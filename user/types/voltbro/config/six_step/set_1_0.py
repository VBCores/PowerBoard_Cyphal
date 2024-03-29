# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/cyphal-types/voltbro/config/six_step/set.1.0.dsdl
#
# Generated at:  2024-03-29 15:42:04.266715 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     voltbro.config.six_step.set
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations
from nunavut_support import Serializer as _Serializer_, Deserializer as _Deserializer_, API_VERSION as _NSAPIV_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import voltbro.config.six_step

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class set_1_0:
    # noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
    class Request:
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
                     new_config: None | voltbro.config.six_step.values_1_0 = None) -> None:
            """
            voltbro.config.six_step.set.Request.1.0
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param new_config: voltbro.config.six_step.values.1.0 new_config
            """
            self._new_config: voltbro.config.six_step.values_1_0

            if new_config is None:
                self.new_config = voltbro.config.six_step.values_1_0()
            elif isinstance(new_config, voltbro.config.six_step.values_1_0):
                self.new_config = new_config
            else:
                raise ValueError(f'new_config: expected voltbro.config.six_step.values_1_0 '
                                 f'got {type(new_config).__name__}')

        @property
        def new_config(self) -> voltbro.config.six_step.values_1_0:
            """
            voltbro.config.six_step.values.1.0 new_config
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._new_config

        @new_config.setter
        def new_config(self, x: voltbro.config.six_step.values_1_0) -> None:
            if isinstance(x, voltbro.config.six_step.values_1_0):
                self._new_config = x
            else:
                raise ValueError(f'new_config: expected voltbro.config.six_step.values_1_0 got {type(x).__name__}')

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Serializer_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.pad_to_alignment(8)
            # Delimited serialization of voltbro.config.six_step.values.1.0, extent 1168, max bit length 1168
            _nested_ = _ser_.fork_bytes(150)  # Also includes the length of the delimiter header.
            _nested_.skip_bits(32)  # Leave space for the delimiter header.
            assert _nested_.current_bit_length == 32
            self.new_config._serialize_(_nested_)
            _nested_length_ = _nested_.current_bit_length - 32
            del _nested_
            assert 528 <= _nested_length_ <= 1168
            assert _nested_length_ % 8 == 0
            _ser_.add_aligned_u32(_nested_length_ // 8)  # Jump back and serialize the delimiter header.
            _ser_.skip_bits(_nested_length_)             # Return to the current offset.
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 1200, \
                'Bad serialization of voltbro.config.six_step.set.Request.1.0'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Deserializer_) -> set_1_0.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "new_config"
            _des_.pad_to_alignment(8)
            # Delimited deserialization of voltbro.config.six_step.values.1.0, extent 1168
            _dh_ = _des_.fetch_aligned_u32()  # Read the delimiter header.
            if _dh_ * 8 > _des_.remaining_bit_length:
                raise _des_.FormatError(f'Delimiter header specifies {_dh_ * 8} bits, '
                                        f'but the remaining length is only {_des_.remaining_bit_length} bits')
            _nested_ = _des_.fork_bytes(_dh_)
            _des_.skip_bits(_dh_ * 8)
            _f0_ = voltbro.config.six_step.values_1_0._deserialize_(_nested_)
            del _nested_
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = set_1_0.Request(
                new_config=_f0_)
            _des_.pad_to_alignment(8)
            assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 1200, \
                'Bad deserialization of voltbro.config.six_step.set.Request.1.0'
            assert isinstance(self, set_1_0.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'new_config=%s' % self.new_config,
            ])
            return f'voltbro.config.six_step.set.Request.1.0({_o_0_})'

        _EXTENT_BYTES_ = 150

        # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
        # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
        # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
        # is not dependent on PyDSDL.
        _MODEL_: _pydsdl_.StructureType = _restore_constant_(
            'ABzY8OyLG*0{`t;U5wmT6`tK>cW3{a-G&yb0@;E@la@~X@9R>DrD=o8bT`AM2^A<9kA1Vp6OV2Dv+RP3QY27<EU{|b3Pc5>0#VVI'
            'mHNON>JwEfDpveFAXM?h8xMKtBM8p5y)(08&m<y<_Msz<$3Evf_nv$HJy(vt@TYrf*(W*S?^vPbH1v=Lw&B>{G};br=%&~8z0i(m'
            'nk=4+g4m4WfIhwB)AV|J>bdmU^kg!nyG9rJpWO1Cs2z9>({nG`n~l)k*29SUjgUr-4f^$%hEbZ-^(`8Nw&$i$OJ*(<_t(?rM6>q2'
            '^tm*d*NrF&>~<W{Fuj<LQmh9`lc_T{b*#QZbGl_jh8{63ag)WzsbhEX2-ab}r*+$PX^_HXPJpT8<D-tSWjLsQ3NtW!peQU{M46>R'
            '_V~amE3vU<8g9c6*tYf-ZG@)b7(wGnH=>&~Af<Ks%Zxg1Z>=<0K4)*b)G8J`e5QH5ZAZF8-OUKnW*tpo8eyb&Jqt~7D!IFLunZGx'
            'oJQUnW1;zL-%U5t<U@E|!?ldS8eHgV+{R-~WkyJoqq^mpX;Mq$wvikk@Rr`*$wT4U6lAzRL~ShU2h=ps_UX0c4*in7O)cH`f=IWm'
            'bUj(tLoW_YiVTP9zJYrsGwjE)+i5b}!pPfhG3s?Z+r-1TH+U@6CVe|i7R((V4Cf){=P*s~_2af<n|eSuV~6e7j{@XQ=RUzj2P`?A'
            '`vpyU;F$*B;2O;SX~fKNTn8gWy#ne+%pqI0Nz-effQnXVJGkzr4&2o@m(JpS=oz(r%#NPQp3mW9;jrY0?)ho5GHQ`<r`z`MP^ifo'
            '?Rppt5oXI-p9V(c1%sh%f{iHv=aOSB!?J95vjl=?7<WB(@WeaATwEdd?hn$F&H8TG#ys`&g)ofbHXgTYyDXyc#@J>zGc2mm(oA|z'
            'r`x{aW~sa$x5IW8Fn6HuE!&JxIm6w=07SbXqn|SOA!xy(5k(Bfo#T`t1GzaWt2U_Nh{Bkh!oZ(B<9J4NC|97-T!Du{1nDa3-!(Q}'
            'JBl$ElG#gvVKO_Td+TS4dlXCV7bQ+0f+#79NMwN!StC5JauQEOiAXZ9Xo4(BT*^{uFl9hVlqa@vA!lbLU>Ol&Jh8l9vGceKA6faz'
            'L%gD@s=zCsUU~4~_9DwMAec|zfjERmuEA&4;ZgYPNmzx?!DDb59)~C3417L0mRsR){6aH}Rd@={W@m;CINu9~FZb@gnllaN`xW#('
            'n9Sv1p?xTRFCh>5UR|cHi8Ui&IU8Y(!U!pO%|qO=(5IM$H$g3jM%Q<ctus>uXs>GAViq5IWOu0-N27MkF`k3L?V5DNN@g5n`J6R{'
            'YRp`&dpCAQ0H&WD!>qTyv^Ij>59j-C(j>-5^n;}sJ{)gs+dOc74X=$2oI88_{U2gy5o?Fetb^r8538*=pW7Zga5%!g3s|^tnivO}'
            'XB!oc9ve_2F?SVr9~to3Cq|72zMUzIv|Ahz#uhV08t3}$p6gc&*Tc8q+t0`owHmK#s-lTJRwG3ad0FKMFUf)`38E^pLM6(Isu51*'
            '@K+XOB1xL2U=`DNRZ<ngF&RPORKj7QlSQH`oJ=%XCW<Jiib7PvtGq065~GSTFNs8u6kJ{s1zr>sLNt8j34)1)Ti}-yWl?3NktiJQ'
            '#&fc&$TE+0lv5Q!k|mAfG)^R%D4?*!skj-DIV`6#FNzwj&2|$7Q9+a-2%1EAMJ61PWlh9g1rbk+N5rEOK@qSROOlF*M`cCSR^<t&'
            '@tUA%gz$pQq3)cZ@I>MTiQu{lsjAl8&8xNWzyq>~r8@iV*Xe)2-)~;073sEfZFMl$Rx#IBhjVS(*EbF9*`>(-8)MqznARBPotY5='
            '!_jFFcmb=T)xg=|I!u{?PQpLo9r!o=t22oK+o`e36uTT@mpZ#l<0Y=JVKP&sA5JSpvL*F{6vPRspM?LFb<YosNq3$0TsF13mGf3I'
            'n~z&qI8v72V^{0kgU87pIv>Tm_X_{+L9nbJiWPX5h6V9TpEv-$QU!gz68d@tbgec~g*`;>gIBA;1LQom;V)Pp|C(3VcQBM{y#Qjd'
            'bGvcYnPc2}c3EJTMZ65e5e~j|J7PTp6-(~MSDgIqGSGn<Y%a>*J5MFY&*MNm>P@Za+<bF_m7lzSR|RN=drK{MFmgY<!A9*3>eI*`'
            '^{#L^AK`~f3LE>ga#HKryjf?A+HRN`Kl2l7>}y}E;1*?PVT(GRX-7Lc=3}`s{Fyc9g9)sUD12ta32>kT&qEhpfa~x>coBXKKZ2jY'
            'OYk%JDf}E>hF`)j;8*Yp{1#q?H{lKV9lQm<hqvJmu;1yRiQtc&E_2)ETXS!6EPuDZy_)ep$?^~IAK>55_zS&}rH&1w-mmr-^4hY5'
            ')TL4n7$$!|2Xjc}%HSb#0d66+RR#}{3$Tw=zYHEC7vNo_?v}wr<N~~h)V(rzh+Kg8k-A?750MM-4W!;EgNMjDcx`C{i}+Hx+m;!H'
            '0LSQDg+Ph%n_Qs9=&cHY5~J9`XLP?ppu{Kyb{T!QLZHMb1ojwxuR@^2C<OKyeZN9rn9+HfjUAcHjm#cL$}+=@0hy&qrtr}UZwxVt'
            '>E~XYem<5@KPRwRcCk^uh)wb(Y>+Qwb9@CG;~Ur%--dncg_rvi(R<KcJKo{psq+PV#v^r_jJbADG>UPk^F_A9|7I5I=)J`|ZM<zh'
            'KW^N~jXY}H**iLN+?jLfH+rxB{l8s0XD9I_%i%4|9}DcC-l5^+>MaZ(ok!Ug1An&^YWB2i{0ErF1YqA8000'
        )
        assert isinstance(_MODEL_, _pydsdl_.StructureType)

    # noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
    class Response:
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
                     log_item: None | voltbro.config.six_step.log_item_1_0 = None) -> None:
            """
            voltbro.config.six_step.set.Response.1.0
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param log_item: voltbro.config.six_step.log_item.1.0 log_item
            """
            self._log_item: voltbro.config.six_step.log_item_1_0

            if log_item is None:
                self.log_item = voltbro.config.six_step.log_item_1_0()
            elif isinstance(log_item, voltbro.config.six_step.log_item_1_0):
                self.log_item = log_item
            else:
                raise ValueError(f'log_item: expected voltbro.config.six_step.log_item_1_0 '
                                 f'got {type(log_item).__name__}')

        @property
        def log_item(self) -> voltbro.config.six_step.log_item_1_0:
            """
            voltbro.config.six_step.log_item.1.0 log_item
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._log_item

        @log_item.setter
        def log_item(self, x: voltbro.config.six_step.log_item_1_0) -> None:
            if isinstance(x, voltbro.config.six_step.log_item_1_0):
                self._log_item = x
            else:
                raise ValueError(f'log_item: expected voltbro.config.six_step.log_item_1_0 got {type(x).__name__}')

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Serializer_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.pad_to_alignment(8)
            # Delimited serialization of voltbro.config.six_step.log_item.1.0, extent 560, max bit length 560
            _nested_ = _ser_.fork_bytes(74)  # Also includes the length of the delimiter header.
            _nested_.skip_bits(32)  # Leave space for the delimiter header.
            assert _nested_.current_bit_length == 32
            self.log_item._serialize_(_nested_)
            _nested_length_ = _nested_.current_bit_length - 32
            del _nested_
            assert 304 <= _nested_length_ <= 560
            assert _nested_length_ % 8 == 0
            _ser_.add_aligned_u32(_nested_length_ // 8)  # Jump back and serialize the delimiter header.
            _ser_.skip_bits(_nested_length_)             # Return to the current offset.
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 592, \
                'Bad serialization of voltbro.config.six_step.set.Response.1.0'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Deserializer_) -> set_1_0.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f1_ holds the value of "log_item"
            _des_.pad_to_alignment(8)
            # Delimited deserialization of voltbro.config.six_step.log_item.1.0, extent 560
            _dh_ = _des_.fetch_aligned_u32()  # Read the delimiter header.
            if _dh_ * 8 > _des_.remaining_bit_length:
                raise _des_.FormatError(f'Delimiter header specifies {_dh_ * 8} bits, '
                                        f'but the remaining length is only {_des_.remaining_bit_length} bits')
            _nested_ = _des_.fork_bytes(_dh_)
            _des_.skip_bits(_dh_ * 8)
            _f1_ = voltbro.config.six_step.log_item_1_0._deserialize_(_nested_)
            del _nested_
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = set_1_0.Response(
                log_item=_f1_)
            _des_.pad_to_alignment(8)
            assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 592, \
                'Bad deserialization of voltbro.config.six_step.set.Response.1.0'
            assert isinstance(self, set_1_0.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'log_item=%s' % self.log_item,
            ])
            return f'voltbro.config.six_step.set.Response.1.0({_o_0_})'

        _EXTENT_BYTES_ = 74

        # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
        # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
        # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
        # is not dependent on PyDSDL.
        _MODEL_: _pydsdl_.StructureType = _restore_constant_(
            'ABzY8OyLG*0{`t;U2GiH6<+7hc486-6N-dNmbQX~gk}Ec4pgd1zz8i4mP1n1DjnUOx!E(@*_qM&ST+?XRH90%k!r{V(KmSDtq*x9'
            'Y6Suzfe_*;Z#?n{stV0J66(1-vp?SPIuTK;KGf3g%$#%Xx##cu=B_X8dHvOeTJJAE8g00V>o@F##UAy&7ii084ciI3QJ8os<M|zD'
            '(>Qa|EN0JbM2uhM$6w|z@?-g4JD^?E|7<Pv(^ecdoG`fPwHt}IZYL>=8VO4qt1OAaAVISkdyU137X}<^`Skhn{wi-yHEVz1FZ29>'
            'P17{?T3N~xet}PlY+%Imy-ObR-C;!gZI`ChPDPlw$sJEH-|J!y?$*Hf*<KK^n8U6@0DJTLq#XRPZKH=ShiRDYhYE8SaMgUddSTR0'
            'M%Nq~G@@8+?5(jz;!vN)ji-Z@wOLFmeui!)B|PxO^TTJocEH@y+19KM*ex%$eHOG+;LRB<hC`Fo?uITF<9L4eO5crG);Nv2Wud|b'
            ')L!AMJiiMQrh!Xichu44tc7XqU88=6`|q*c(BXNFXDym9jP%QHZ4}e+A_pBFOfVXkMKN<IR-a$V584;Kb>`Yp7^k-9@-z8iI|;Mc'
            'VW{w#9Z}pXpB5M2Yw>(`1&42aMM$q=Zc~ro-Vlmu+ZA~{pK~@Mp#H<6(+SV-jk1>SId;t2nJ;!6&H-xo6+J<xBbD4&^aV@W?@U8('
            'NDWbco{DlT*gzAED`r6|8nWg&j9&o*Osqo7N52pB+chkgEk=Iq8KXVrrO))9&*Ed*uza^2Mm(=ia*}LxTOlTeku0-rh{KQ~UY?Cu'
            'Ow%wP9cBkS1Oc4Q53Nww^@4WA2%Z<(GntPWZ;WfvL($zo@ng-I&7_4$jS5FNMp+Bf?RtTjD7>NT;$~V*6;@iT-fy$@hz30{pUGND'
            's~8wBu?5nxT=+ah%KfN2fI1vC-xoVnEQVORZxWVP8TD0V2PEOR&o22PO}8Kf8qGR90xD>iG3qXD2VR;X0`l35F?B?Bv8gjl<vlLT'
            'A5=9-A&ROQhDvmW5ZxlOY)YC;RE=o5Y*>n}X%ZIz8U+d%x$)#WI`TK_vA{usQzXz__ljvt9<BfSVc9TEQ<066^%MQu3j$d{5JkU-'
            'EP+R_z+-3N=kSYTun3RCDL4&Jz>}~9PvwV-Dr}uvX!a%)o`Gk3Im0TP8;roO26w+HlvH%QjvWU_G#Xs255vzz)WNWqb19A63_%bv'
            '#B!x!p-6iN-G1gX$4-Hzbf<3Le-q~1x#1@&E#BG=v29V;ci`<E>w4#4zyCsMcdz_%dHbsEe%gL~qUO{@&FQM<NO^b9NU?u1>2()*'
            'F0!a#>05l^?Fdps+o@;kgPtvxJ%iuDOV8_5wVG^NreUcvqRdcKSvMsjYr0};ifXC?fU0ho7LiN|uezcWO|vWm(P_!1W*S5iYZOB='
            'iG%>wRbm>FPApv~hN_r`K};f>vaU&*kgB?@sYKBXbg!w3tSSZ}7Cy=ZjfsX^;73w*)fA8?hJ?Gxl5QHhE+aokrlDxMW=WDIsl-wh'
            'T&zhZZbozoX+oD()k5E5H&sy$v{Dqs(ui#6L?XIwskp16Vz!tfrcM+?L6Xrl6O+eaRgBh@iDb!^Vp)X9iY{U7l48h2lNF7iUxRGN'
            'LekAyNO|ZXT}2A&U5EVh1zf*5{}|eBgJf|OB#Q`=#c_}v>_r<>-)3=)@2$#&e~w1`5<D4Ezf>}j!ZG*?K7)V2*V#6C<kKYt@cmbS'
            '0J*;p1AONWf$)PeJU8;<J#sn>#5pL~_6?rT7B6r-XK(?s?Yw<Cp+N8@ON8_iN-qtiedDd-qMGmtBJ$G$&!559H!l?Y6TX3O;a?-k'
            '<NKejV?HTwUdr#rgI;mUj%{Gn#Y=JiKAta}3zCWF)sm{^=9C!Qg0QzO>UV|cdl7MkT}SKuqg5KT*(!@z>P<Q;{kAy5%#RJBIQH~P'
            'R_m9nIV0q?&7@bmqRfKA->NFhF+H@#{Lt~zjRAp<&*?{En4K){9VxdMm2L3gDEQEU*Psip!&P__-hjWtpW$!tF1!bShY#TW&IzPP'
            '_^{K!OXnnhP3~EKxc}qjHb;201OK=DU$Q(u!1@f%=FE@+&KDCqkJ9-nF^q}-SQtwvm8!;L;?j5pr7KnAF>z@ep){%*kBR?M7;mC<'
            'vuZphE<ImE>9wlyn7A~)j?(K@<1uk*d;_I7s>WNzog;|Ap8fLt6tLyZsmh9qVq}dZRMM{MnsG(R-S;AQ|G41pqev57q=+|=9^OT2'
            'cpo`I(7}I%Njeg$N2sH70G~0w&YW0#5Whw_y>q8<e7l6+sSn(Ceu}rvr5!lCtkne4US8QXk+o-r|KJ(^Na%blGB}(}rq(&}8-0vb'
            'FW&;IcCHD}BfkmC*ajgr{tb$>8H}70000'
        )
        assert isinstance(_MODEL_, _pydsdl_.StructureType)

    def __repr__(self) -> str:
        return 'voltbro.config.six_step.set.1.0()'


    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8OyLG*0{`tATWlOx)sHydI8JOQG$1O9TcQw3yUcrLTM$mu27>E!aY9lWMZ@gw&EA>J&P--zT{~5fqe7dYk!m#q1tL%@5EY0D'
        'i?4q0QK_GeN~ownd>~Zu#aH;uALs1M&aUUNu}IVe6iYrca~}6`-uK$8TYgCP4RwBk&pIm&uVI!|kGQ&K>gTkYNy=*7ZaKE6`y>pu'
        'A0_URUMI&^91>m*zi=TuAMOu!s4h9%CZ4bQh^Irrj-$TYuKR5_#W|*0S_{Vc+>&kjHP<fJZR@n&EPML0>iNVed&Dm<MuUYxNnIkY'
        'r`r||Iet8TzZ}jF&kwy6UV!DOn(w=Mt?d&pJQWsgAYlrFu|qmB8@&Zhs1426dh33Yn0gDg+Ss`6t*UNW#0}|qgrF0_14Ua{(o9%>'
        'NGIve?n3FzDUi7@mi<)UD6?&CsjgXN$Hi&&B~te4nyI<v!<J8)#8oom^oA+gZZcLF%pBF57HPzTZQRp#wWj;3Nvx(%!}$`ZqOO4n'
        'TXq9fQ4aQ0yThPZ`5@31kOb-<`hK_=2A_cKYF0yY8~p=aY}a60V;v=g!4|b)*TY~aY}d44cb~P?+DhaK=R^7!eZ+&+G>GGpx(2!r'
        'F9kc*)A}-LsE+OWs@@2X1T(5<x7|7cf=N_IgSmone3*JI47OFlLzk<Fy$pLB{u0bhZFIE}M-PL^`ies}^HH?37Y6q`?V73A!EKvu'
        '6KCvs0Z_L_Hi1F=G`Tgh3#hbfnKD~u%BcU)M|JF0spi4DTw?iX5Db&>5`CP08MII{VcdOPbM@4vqQ9rUVYN@_{?ncBqwpCUEErX7'
        'Ck$qb2Ju!}H5)bsD_I~d8=S$1XnDpVuIAfrzbn_N4k19F4W_DEqoG^P3==(t)FW*ZcD$0N!U&OdUkUfmm)5)*#HkYv1a8!>!FF4^'
        'g&qYj+A_Y3qgR2ZQF=lp%Z_GsLitF$=G8h5vlDFJ(Ca=dPP3ZefS@-Z^g?DIFikdyPk;yf&NQ<ueX&^-Rf|M3d2T>Vf#YvGWZIg)'
        'Ayz0qKT8Fw(8@(ve@kmxy5ELa2)3PewL0n<%v(AXzk^utd0t>Rh2sTD;uVoo6tSYPtjq|k!V8KZvQmW;1%U}Ml=?%4J|0L<EyF<O'
        '%B+hK;ekJ4T+ix}-+7PCo_v&*WLf4|>5<tlc3)3njM1+^JiScMdGxE7=-d%{fIhjOK1C1FuhFm5!}J?;o<1E+MOxVCzqH!%Rr*bO'
        'tg~l&f<BixgPOe6BjRba{Vdp?QZzZ$K|coko&j2`XVn>E)gfoN7_&a)DDaSs)qLQa@*Dy|coVJ}Pir|QkX2NL3;N3E+tKk4)z@3Z'
        'Zu><uMm)9&&TZ96!ASMC+ll8+QOM_+h}Pa}n*|J84-X)gswWl-$US#{@FqoKutzf)AKvJ1IBn!Of1qy<bevtud>@1F?10>%qIMwt'
        's9wJIwnw^$3hWi=cM=j8bQ6PEw&O&xp$9rtA<w7dx6kz1?4hFez|lJk2HYlFgn`LS5(b(6d}8{!*z|OjzWA&-JT%106<MnAEMy~z'
        '<5^K=6jl&9S>Sk?$3(@8l3Y<3nSrOsiHaapDiUO|3M&h;q%bJMNsO#8kmy8SktIe{Dx#=JJSR(%A}g%SiUK1bmKRxpS2#g};RT*!'
        'c}`N43VgB(Fe?H~0ly3{@-n7IMPgt!mJwx16j{ilj4W}2C{!4x!thFk=RjCsWSC458Azuh%kvc&8)xG=UIH$T<0^u}N}|FjqFCW!'
        'R*r|=!WLoc3MX-pj0Hi4&BJ1OSgp(|Oogp*m5QRUoXEi18BSsqf#n1R#+8)3Y|Y#}TXPRTEb@@5JI`L8{x|*C&GWP*+;XhV^~c&A'
        '#M)ds*0wroQ-hkF@$7#hQ6EHX3?T06D8bcCmAJ0$ViwJ3+?LM61QoR37zRhB9~oQVVT>RcM=*w90znDE4g}i)v~!dhjK^^ZZA%<='
        'L8%*y&?@z!@xM~@bAA2NeFtp|+gB^M@d~y@eHUbq5F>ryXvPDuoz92xAiUiv{u^DdIkLfN=ndk<$kiUQk99SV^_^VScXC)4hKBQa'
        'H=ujWbNS4D=*Y?G-yu={BTBO$Mcy=)_z=3!ZSy%}3aQfwW)SQG(C1Uo4U=Ub3kfVT*aPRD=*a1+lxWy2MTgOHu=`ukB^Mpv;&Lv{'
        '4`WV>ih7>2=9oHDhx@(wlZ)7YFA|6NdeH&mOw`w>^9-H^Iyq)2(f@o22}5gM#}FNxVYOfQP7XEBMUzX!wClRRqC#wD)5YJgVt3oJ'
        '9!F$6YSF#)EVb!t)TKYAKc+vUSLo~X=kyo!4f-qkOZsd2CjBk_4gDQ`i@rzK>HG95{S*Bo{WJZ5{)K*M*l7H}8ZMg6*_?TUsp!Ce'
        'Yx(0YiTHc`_xSH-{*y@`Q-b1A>Sg|uQEr(A>~y9cq|vWL%nV?eEOQDSGgkpy%`&IZF|z|$C(E2d$INShUCT13&@uBmVAr$EDRj(y'
        '4Y1d;%qeutd>ydYv&<=U#Jn&)3`u-CTY0mDSb#x1lOvEJyc-Er5ns&_$PnTg9K<_00vSRqu!i`x9DxiW7Fb98dX7Mb5DQ#G{Iwi`'
        'G{N{b_8%RY>m7ZJW@XZZKAGteT=140YorKqCo~J4&_hutv=@q{3x)Cu6v;QBK)wmZ@hvEfSD`3=KtF_9=p?Ptov5yczp;5To`G-J'
        'l2JwCVmE2T?T~RCXShARkkLp6H=6J||LUN2CsJ}zyR*Kfu-%!k$n(j4K<_TbI5q-1+2d`Z|Cq$<-&FH)aTCplaR8_2yMu|BnXE3@'
        'sltKQu`Q3pJ!$V!V(;KT;6ze*H8GvKlE}L&nJpU3w3{k)#;t)jC3rJDrhBSw<=+}_2U_O>r|@EN(%0N3@zu_4Qa;Pr0NMmGNnQ0R'
        '@wF_&?}1^odSW48bo8)#ppf!JA?4t0xPx*D{%vKTX7OmgbK@Dl;1&SSDamzge31GPxR((k_z8m7MmE<@@9r(`V`-^x6kLtOM@%@('
        '<{fiW=qQ+tHH@f9<5hg1E~D+^&TmO4#+8w55}aSX137SdKn{%5QIG=XUoXsnQ^|p^>yjxKGXm5nxMKI%w}CI#>{-;Ojlf6XB6uD_'
        '8^JjQ%LvXRcmcsGg6|@D5y1rnFCq9If=dWqM(`ejA0T)i!PQOr@k}>)-8&fG<NyCY$h`Z%caSmO9!a|AqH{o+&?gg}T1JYFGb8E3'
        'a3(4Yt)wv6Ns?+Osp*9zAzet)(922kx!S8DcU!JAuI1Dx(83)kP=^LJ>5*NEn)K>OVTmgB8qvNMy*>)NBe3;Nbm_+NL`9qG&8wrS'
        '-n^Rjso?$rEqKy-_qTH;5E_sFQ!86!wW!FJ+@yK$FRw1{)j`lk;Eit1F^+F^jCQU39|zfYVsIt^00'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)