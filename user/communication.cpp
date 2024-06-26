#include "main.h"
#include "hmi.h"

#include "voltbro/utils.hpp"

#include "cyphal/cyphal.h"
#include <cyphal/allocators/o1/o1_allocator.h>
#include <cyphal/providers/G4CAN.h>
#include <cyphal/node/registers_handler.hpp>
#include <cyphal/node/node_info_handler.h>

#include <uavcan/node/Heartbeat_1_0.h>
#include <types/voltbro/battery/state_1_0.h>
#include <types/voltbro/battery/buttons_1_0.h>
#include <types/voltbro/hmi/beeper_service_1_0.h>
#include <types/voltbro/hmi/led_service_1_0.h>

TYPE_ALIAS(HBeat, uavcan_node_Heartbeat_1_0)
TYPE_ALIAS(LEDServiceRequest, voltbro_hmi_led_service_Request_1_0)
TYPE_ALIAS(LEDServiceResponse, voltbro_hmi_led_service_Response_1_0)
TYPE_ALIAS(BeeperServiceRequest, voltbro_hmi_beeper_service_Request_1_0)
TYPE_ALIAS(BeeperServiceResponse, voltbro_hmi_beeper_service_Response_1_0)
TYPE_ALIAS(PWRButtons, voltbro_battery_buttons_1_0)
TYPE_ALIAS(BatteryState, voltbro_battery_state_1_0)

static constexpr micros BATTERY_INTERVAL_MICROS = 200000u;
static constexpr micros BUTTONS_INTERVAL_MICROS = 200000u;
static constexpr CanardPortID BATTERY_INFO_PORT = 7993;
static constexpr CanardPortID BUTTONS_INFO_PORT = 8003;
static constexpr CanardPortID SRV_HMI_LED_PORT = 172;
static constexpr CanardPortID SRV_HMI_BEEPER_PORT = 258;
const std::string battery_serial_number = "H000061";

class LEDServiceProvider : public AbstractSubscription<LEDServiceRequest> {
public:
    LEDServiceProvider(InterfacePtr interface): AbstractSubscription<LEDServiceRequest>(
        interface,
        SRV_HMI_LED_PORT,
        CanardTransferKindRequest
    ) {}
    void handler(const LEDServiceRequest::Type& led_msg, CanardRxTransfer* transfer) override {
        int beeps = -1;
        if (led_msg.duration.second > 0.01) {
            beeps = (int)ceil(led_msg.duration.second * led_msg.frequency.hertz / 2);
        }

        start_led(
            (HMI_LED)led_msg.interface.value,
            (RGB){
                .r=led_msg.r.value,
                .g=led_msg.g.value,
                .b=led_msg.b.value
            },
            beeps,
            led_msg.frequency.hertz
        );

        LEDServiceResponse::Type response = {};
        response.accepted.value = 1;
        interface->send_response<LEDServiceResponse>(&response, transfer);
    }
};

class BeeperServiceProvider : public AbstractSubscription<BeeperServiceRequest> {
public:
    BeeperServiceProvider(InterfacePtr interface): AbstractSubscription<BeeperServiceRequest>(
        interface,
        SRV_HMI_BEEPER_PORT,
        CanardTransferKindRequest
    ) {}
    void handler(const BeeperServiceRequest::Type& beeper_msg, CanardRxTransfer* transfer) override {
        int beeps = (int)ceil(beeper_msg.duration.second * beeper_msg.frequency.hertz / 2);

        start_beeper(beeps, beeper_msg.frequency.hertz);

        BeeperServiceResponse::Type response = {0};
        response.accepted.value = 1;
        interface->send_response<BeeperServiceResponse>(&response, transfer);
    }
};

extern FDCAN_HandleTypeDef hfdcan1;

static constexpr CanardNodeID NODE_ID = 9;
static uint8_t CYPHAL_HEALTH_STATUS = uavcan_node_Health_1_0_NOMINAL;
static uint8_t CYPHAL_MODE = uavcan_node_Mode_1_0_INITIALIZATION;
bool _is_cyphal_on = false;

static std::shared_ptr<CyphalInterface> cyphal_interface;
void cyphal_error_handler() {
    _is_cyphal_on = false;
}
UtilityConfig utilities(micros_64, cyphal_error_handler);

ReservedObject<NodeInfoReader> node_info_reader;
ReservedObject<BeeperServiceProvider> beeper_provider;
ReservedObject<LEDServiceProvider> led_provider;

static uint32_t uptime = 0;
void heartbeat() {
    static CanardTransferID hbeat_transfer_id = 0;
    HBeat::Type heartbeat_msg = {
        .uptime = uptime,
        .health = {CYPHAL_HEALTH_STATUS},
        .mode = {CYPHAL_MODE}
    };
    cyphal_interface->send_msg<HBeat>(
        &heartbeat_msg,
        uavcan_node_Heartbeat_1_0_FIXED_PORT_ID_,
        &hbeat_transfer_id,
        MICROS_S * 2
    );
}

void user_setup(void) {
    setup_hmi();

    cyphal_interface = std::shared_ptr<CyphalInterface>(CyphalInterface::create_heap<G4CAN, O1Allocator>(
        NODE_ID,
        &hfdcan1,
        200,
        utilities
    ));
    node_info_reader.create(
        cyphal_interface,
        "org.voltbro.power_board",
        uavcan_node_Version_1_0{1, 0},
        uavcan_node_Version_1_0{1, 0},
        uavcan_node_Version_1_0{1, 0},
        0
    );
    beeper_provider.create(cyphal_interface);
    led_provider.create(cyphal_interface);

    HAL_FDCAN_ConfigGlobalFilter(
        &hfdcan1,
        FDCAN_REJECT,
        FDCAN_REJECT,
        FDCAN_REJECT_REMOTE,
        FDCAN_REJECT_REMOTE
    );

    static FDCAN_FilterTypeDef sFilterConfig;

    HAL_IMPORTANT(apply_filter(
        &hfdcan1,
        &sFilterConfig,
        node_info_reader->make_filter(NODE_ID)
    ))
    HAL_IMPORTANT(apply_filter(
        &hfdcan1,
        &sFilterConfig,
        beeper_provider->make_filter(NODE_ID)
    ))
    HAL_IMPORTANT(apply_filter(
        &hfdcan1,
        &sFilterConfig,
        led_provider->make_filter(NODE_ID)
    ))

    HAL_IMPORTANT(HAL_FDCAN_ConfigTxDelayCompensation(
        &hfdcan1,
        hfdcan1.Init.DataTimeSeg1 * hfdcan1.Init.DataPrescaler,
        0
    ))
    HAL_IMPORTANT(HAL_FDCAN_EnableTxDelayCompensation(&hfdcan1))

    HAL_IMPORTANT(HAL_FDCAN_Start(&hfdcan1))

    _is_cyphal_on = true;
    CYPHAL_MODE = uavcan_node_Mode_1_0_OPERATIONAL;
}

void report_battery() {
    BatteryState::Type battery_msg = {};
    static CanardTransferID battery_transfer_id = 0;

    if (prime_VIN != NULL) {
        battery_msg.voltage.volt = prime_VIN->LPF;
        battery_msg.current.ampere = -((3.3 * (float)ADC1_buf[1] / 4096) - 1.655f) / 0.0264;
    }
    else {
        battery_msg.voltage.volt = 0;
        battery_msg.current.ampere = 0;
    }
    battery_msg.charge.coulomb = 0;

    battery_msg.design_capacity.coulomb = 0;
    battery_msg.capacity.coulomb = battery_msg.design_capacity.coulomb;

    battery_msg.power_supply_health.value = 0;
    battery_msg.power_supply_status.value = 0;
    battery_msg.power_supply_technology.value = 2;
    battery_msg.is_present.value = prime_VIN != NULL;

    int connector = 0;
    if (prime_VIN == &VIN1) connector = 1;
    else if (prime_VIN == &VIN2) connector = 2;
    else if (prime_VIN == &VIN3) connector = 3;
    if (prime_VIN != NULL) {
        sprintf((char*)battery_msg.location.value.elements, "%d", connector);
    }
    else {
        sprintf((char*)battery_msg.location.value.elements, "None");
    }
    battery_msg.location.value.count = strlen((char*)battery_msg.location.value.elements);

    sprintf((char*)battery_msg.serial_number.value.elements, "%s", battery_serial_number.c_str());
    battery_msg.serial_number.value.count = battery_serial_number.length();

    cyphal_interface->send_msg<BatteryState>(&battery_msg, BATTERY_INFO_PORT, &battery_transfer_id);
}

void report_buttons() {
    PWRButtons::Type buttons_msg = {};
    static CanardTransferID buttons_transfer_id = 0;

    buttons_msg.emergency_button.value = (emergency_stat != 0);
    buttons_msg.user_button.value = HAL_GPIO_ReadPin(GPIO4_GPIO_Port, GPIO4_Pin) != GPIO_PIN_SET;

    cyphal_interface->send_msg<PWRButtons>(&buttons_msg, BUTTONS_INFO_PORT, &buttons_transfer_id);
}

static micros battery_report_time = 0;
static micros buttons_report_time = 0;
static micros heartbeat_time = 0;
void reporting_loop(micros cur_micros) {
    if (!_is_cyphal_on) return;

    EACH_N_MICROS(cur_micros, heartbeat_time, 1000000, {
        uptime++;
        heartbeat();
    })
    EACH_N_MICROS(cur_micros, buttons_report_time, BUTTONS_INTERVAL_MICROS, {
        report_buttons();
    })
    EACH_N_MICROS(cur_micros, battery_report_time, BATTERY_INTERVAL_MICROS, {
        report_battery();
    })
}

void user_spin(void) {
    micros current_micros = micros_64();
    reporting_loop(current_micros);
    hmi_interrupt(current_micros);
    cyphal_interface->loop();
}

