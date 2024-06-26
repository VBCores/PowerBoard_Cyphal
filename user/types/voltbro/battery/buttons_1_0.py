# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/cyphal-types/voltbro/battery/buttons.1.0.dsdl
#
# Generated at:  2024-03-29 15:42:03.544204 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     voltbro.battery.buttons
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations
from nunavut_support import Serializer as _Serializer_, Deserializer as _Deserializer_, API_VERSION as _NSAPIV_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.primitive.scalar

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class buttons_1_0:
    """
    Generated property settings use relaxed type signatures, accepting a large variety of
    possible representations of the value, which are automatically converted to a well-defined
    internal representation. When accessing a property, this strict well-defined internal
    representation is always returned. The implicit strictification enables more precise static
    type analysis.

    The value returned by the __repr__() method may be invariant to some of the field values,
    and its format is not guaranteed to be stable. Therefore, the returned string representation
    can be used only for displaying purposes; any kind of automation build on top of that will
    be fragile and prone to mismaintenance.
    """
    def __init__(self,
                 emergency_button: None | uavcan.primitive.scalar.Bit_1_0 = None,
                 user_button:      None | uavcan.primitive.scalar.Bit_1_0 = None) -> None:
        """
        voltbro.battery.buttons.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param emergency_button: uavcan.primitive.scalar.Bit.1.0 emergency_button
        :param user_button:      uavcan.primitive.scalar.Bit.1.0 user_button
        """
        self._emergency_button: uavcan.primitive.scalar.Bit_1_0
        self._user_button:      uavcan.primitive.scalar.Bit_1_0

        if emergency_button is None:
            self.emergency_button = uavcan.primitive.scalar.Bit_1_0()
        elif isinstance(emergency_button, uavcan.primitive.scalar.Bit_1_0):
            self.emergency_button = emergency_button
        else:
            raise ValueError(f'emergency_button: expected uavcan.primitive.scalar.Bit_1_0 '
                             f'got {type(emergency_button).__name__}')

        if user_button is None:
            self.user_button = uavcan.primitive.scalar.Bit_1_0()
        elif isinstance(user_button, uavcan.primitive.scalar.Bit_1_0):
            self.user_button = user_button
        else:
            raise ValueError(f'user_button: expected uavcan.primitive.scalar.Bit_1_0 '
                             f'got {type(user_button).__name__}')

    @property
    def emergency_button(self) -> uavcan.primitive.scalar.Bit_1_0:
        """
        uavcan.primitive.scalar.Bit.1.0 emergency_button
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._emergency_button

    @emergency_button.setter
    def emergency_button(self, x: uavcan.primitive.scalar.Bit_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Bit_1_0):
            self._emergency_button = x
        else:
            raise ValueError(f'emergency_button: expected uavcan.primitive.scalar.Bit_1_0 got {type(x).__name__}')

    @property
    def user_button(self) -> uavcan.primitive.scalar.Bit_1_0:
        """
        uavcan.primitive.scalar.Bit.1.0 user_button
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._user_button

    @user_button.setter
    def user_button(self, x: uavcan.primitive.scalar.Bit_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Bit_1_0):
            self._user_button = x
        else:
            raise ValueError(f'user_button: expected uavcan.primitive.scalar.Bit_1_0 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.emergency_button._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.user_button._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 16, \
            'Bad serialization of voltbro.battery.buttons.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> buttons_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "emergency_button"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.primitive.scalar.Bit_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "user_button"
        _des_.pad_to_alignment(8)
        _f1_ = uavcan.primitive.scalar.Bit_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = buttons_1_0(
            emergency_button=_f0_,
            user_button=_f1_)
        _des_.pad_to_alignment(8)
        assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 16, \
            'Bad deserialization of voltbro.battery.buttons.1.0'
        assert isinstance(self, buttons_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'emergency_button=%s' % self.emergency_button,
            'user_button=%s' % self.user_button,
        ])
        return f'voltbro.battery.buttons.1.0({_o_0_})'

    _EXTENT_BYTES_ = 2

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8OW_7)0{?YXZEF)j5Ke2;^i54^tzZTHB(2h`?;jOfEG@AySgDGZW$$jyEbQGLyL%xK3ig9SU_qhl|8+K(*V+a`c4uavnR%X>'
        '{FwQ>Rxb5E_FmSBbu0p+nc`IN?=%!FAdyTmskvd!UOzG_k4&!Ehfc=ax!XK*r*6ZRNlFv+-)>1^LM4Nc8pBj42y<g(s-2x9Ev7V='
        'se_WO9QV)Xt~OOG{c>l{E)smAI6h$7ogn5F)eNJYE$?wA;!za~B&LQE<4c3-!U$!%p3_!D(;!nk;fA+Zpd%`%3U;`0P=WbD4X||L'
        'pxS@8a#aCC7_50mO2KG4NyZ`xxgmn3O#|2;mK9NLNFrk_>#kjE3;_JIU>ALd-i2J0e!BP0t`co%8dDXI19kHddnvc5$T9N_iDl$$'
        '$>kxnD`V7=uv2Jp>R<!zXsjk?nPL$&EOuRcgM8y{7L!aWLwM}!cA03ItB9dPFp^QsWh?$i@X*=$21?&<c<VX#HnokpL3*vHGw$qC'
        ')X9K~Ezdcsyq@Ku;1N-*nG2tBqzHOv3n376jKkSN41_{Cf+xY_z?1HbXJUl_)mV~Zsqrebc*I;6HsK)>5DJ8RFwkhk6b71$_X7QG'
        '?|y{WzE<`ck(smiuL9AXB$U_>R&vM^i4$OOYTso{Q6tqz@mUf9$4P`ed$U2~n5WJEf}rNT^;}@Hor_*XD1`m(HfmFUbcp+s6+o^w'
        'mxtJH!c#o@18w_5#Savc>|ZYs*3M|!Td8^;>aaH}RhBT-WNFkP#Tq)#9J+=h4yzcpm?N{35ey!A|5sQB0w+0abs?z3Hay*cXYd?e'
        'z)M@{Z#vFOf7hL@_P2dfMR?Uy3|_-dFE6}-{UIfX!_)p4O}BPs>IXKxly5s<(2Y~!|0pg+JAh-)8+@$I!6*EF#=KvU8aQCuTdQcT'
        'j;w>=NweoM_y@q8Y|9}9000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
