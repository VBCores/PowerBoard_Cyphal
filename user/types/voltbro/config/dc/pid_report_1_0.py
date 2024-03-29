# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/cyphal-types/voltbro/config/dc/pid_report.1.0.dsdl
#
# Generated at:  2024-03-29 15:42:04.152165 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     voltbro.config.dc.pid_report
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
class pid_report_1_0:
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
                 integral_error: None | uavcan.primitive.scalar.Real64_1_0 = None,
                 signal:         None | uavcan.primitive.scalar.Real64_1_0 = None) -> None:
        """
        voltbro.config.dc.pid_report.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param integral_error: uavcan.primitive.scalar.Real64.1.0 integral_error
        :param signal:         uavcan.primitive.scalar.Real64.1.0 signal
        """
        self._integral_error: uavcan.primitive.scalar.Real64_1_0
        self._signal:         uavcan.primitive.scalar.Real64_1_0

        if integral_error is None:
            self.integral_error = uavcan.primitive.scalar.Real64_1_0()
        elif isinstance(integral_error, uavcan.primitive.scalar.Real64_1_0):
            self.integral_error = integral_error
        else:
            raise ValueError(f'integral_error: expected uavcan.primitive.scalar.Real64_1_0 '
                             f'got {type(integral_error).__name__}')

        if signal is None:
            self.signal = uavcan.primitive.scalar.Real64_1_0()
        elif isinstance(signal, uavcan.primitive.scalar.Real64_1_0):
            self.signal = signal
        else:
            raise ValueError(f'signal: expected uavcan.primitive.scalar.Real64_1_0 '
                             f'got {type(signal).__name__}')

    @property
    def integral_error(self) -> uavcan.primitive.scalar.Real64_1_0:
        """
        uavcan.primitive.scalar.Real64.1.0 integral_error
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._integral_error

    @integral_error.setter
    def integral_error(self, x: uavcan.primitive.scalar.Real64_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Real64_1_0):
            self._integral_error = x
        else:
            raise ValueError(f'integral_error: expected uavcan.primitive.scalar.Real64_1_0 got {type(x).__name__}')

    @property
    def signal(self) -> uavcan.primitive.scalar.Real64_1_0:
        """
        uavcan.primitive.scalar.Real64.1.0 signal
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._signal

    @signal.setter
    def signal(self, x: uavcan.primitive.scalar.Real64_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Real64_1_0):
            self._signal = x
        else:
            raise ValueError(f'signal: expected uavcan.primitive.scalar.Real64_1_0 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Serializer_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.integral_error._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.signal._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 128 <= (_ser_.current_bit_length - _base_offset_) <= 128, \
            'Bad serialization of voltbro.config.dc.pid_report.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Deserializer_) -> pid_report_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "integral_error"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.primitive.scalar.Real64_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "signal"
        _des_.pad_to_alignment(8)
        _f1_ = uavcan.primitive.scalar.Real64_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = pid_report_1_0(
            integral_error=_f0_,
            signal=_f1_)
        _des_.pad_to_alignment(8)
        assert 128 <= (_des_.consumed_bit_length - _base_offset_) <= 128, \
            'Bad deserialization of voltbro.config.dc.pid_report.1.0'
        assert isinstance(self, pid_report_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'integral_error=%s' % self.integral_error,
            'signal=%s' % self.signal,
        ])
        return f'voltbro.config.dc.pid_report.1.0({_o_0_})'

    _EXTENT_BYTES_ = 16

    # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
    # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
    # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
    # is not dependent on PyDSDL.
    _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
        'ABzY8OyLG*0{?|oYj4y>6y3Ctgg1ynTeT|77aAyR$77E@rc#?ii_|WJC@BcFqSn}+>>cX0T|c61C8Y476_G|N64USfslBt#V*^Bu'
        '6nQ*%=G=Ra&$+vO>>p>bH~rIB%1K(M*&wQAr9`Iw5OF34QBsV{qE?MG`pkDSQ)67FKTS$$UYqML%yYA(=OdNpvNF)qXV#mlO`5in'
        'hmRbOaxq4TPdAIKiK}9e6#0f44bo&#sx+!(SyYYDi_xa6YE|SGYvJ+k`n4I(4SRo?7e=3oMAK9%ZW~#frwDvR)%&N6K7LQhEIlaY'
        'WR!|VM2)Qv7P?J1sXuGQW+L)IS=koVrX19X$V4?*lOppy1E=BaUKw!VsewzoS3f$chJ7TXPu$B2(Hy4aR1~Ww%49xjzzmnMu0+&L'
        'G%ixC>#DxIx_8}P8{Ea%0~<mzdViWVqd$o1M&zle(pjLFh%*+WTs3WK6K_-^X^_Mk$-TF`MvNzHuGe#dFz`dyaXs!+*I@zSj>l-='
        'Q8#d%fOszRgOHPe;FD3tJueJ>7V^*uyujzg-l0ATI3biXmj^y!JY<afE)9I22iyr9<`K{Cy3FxhPCXytJ(oHz^*Imm)!}%Udzb?M'
        'iObx8Iey4}g4rCx0-rI5a!LZ9ddv$635m-?m*QoQ1elC7!aY3Xx*=lQY%X<uJVhxDJ?{976V6!ZVpi&6x7Z@K&Z$p{=XhR#&111H'
        'RvS2+gic7qkaLGJg0&OsJKS@q#}U`(#**L0sF>rMB5RT3V^LZpMw9Qiklt+4M=@8jmU&}k&{ugQM=0dm{a<d;8#kDHv;W2P`4mxv'
        'zBnW3D4ujSd2YaiD>X_awOENj%b6X0Hrh~IGL5WPB9)pIeIcrgwn`)hG8vTu1)vw~BU3Sc{8cpW)~eloje?u|5^IIR+VH(n8GSmL'
        'lpwNO)(I$&Ps%pVRDxa{wVBO$;1i6_clJQg8ClPF7BTu<XOe+4AOmX!(^!RGj6l>_RfSwwZ)~bWnjK)eXGx1QguS+BodXHu$>z;>'
        'EcT9S?oZ#>@pack`u(UVjqV=>QcuQlfjwa<59GK&V_Nw?EM+B{qM99G2`HQqu&&RoiZoUE=&eKW#70-z3>%)j8AXIn41b%Y;qt3G'
        '#z|IoKxVku#@Oyy<<{l65L<S!V4aRc+uJ82xmAjMI_y^3xQ?g#Iy;q4C9+6X73Km4Lk#TC9rzdz&DUy_i)=S2A+R9@mmz~^ErdI8'
        'dj-CNub1E(ScY%mj$YWEz*uuPgHa8sW$0iIAO4K+<BkP~`|xm@8P?#@J|#czuO7|Nbm?x9ThZq4<XfNU=tf!C5&llJ$B<awARR7)'
        '#QzP<3rGz-mbKm8#@+3M-Mzzyw>uu;6prrmc4RLhEzka+BFLeD5`Ld)9>12{!hRYv+}4-TmEG@P6@e5fKDr;1tNP-j+<p(4{?NJp'
        '(8Pyp!#;ct*N1a<guu<0Slv5Geco+t+lqhf*1`&_kHR{{^M`99AIUXY%0?Zf?B6=UoyQBaSc|Ww?4-lq9%aKtyWe|NPr2)8?ql%Z'
        'w}bZT;6G=v>a9Eo000'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)