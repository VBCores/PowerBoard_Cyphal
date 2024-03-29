# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/cyphal-types/voltbro/echo/echo_service.1.0.dsdl
#
# Generated at:  2024-03-29 15:42:04.050107 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     voltbro.echo.echo_service
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations
from nunavut_support import Serializer as _Serializer_, Deserializer as _Deserializer_, API_VERSION as _NSAPIV_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.primitive

if _NSAPIV_[0] != 1:
    raise RuntimeError(
        f"Incompatible Nunavut support API version: support { _NSAPIV_ }, package (1, 0, 0)"
    )

def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))

# noinspection PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class echo_service_1_0:
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
                     ping: None | uavcan.primitive.String_1_0 = None) -> None:
            """
            voltbro.echo.echo_service.Request.1.0
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param ping: uavcan.primitive.String.1.0 ping
            """
            self._ping: uavcan.primitive.String_1_0

            if ping is None:
                self.ping = uavcan.primitive.String_1_0()
            elif isinstance(ping, uavcan.primitive.String_1_0):
                self.ping = ping
            else:
                raise ValueError(f'ping: expected uavcan.primitive.String_1_0 '
                                 f'got {type(ping).__name__}')

        @property
        def ping(self) -> uavcan.primitive.String_1_0:
            """
            uavcan.primitive.String.1.0 ping
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._ping

        @ping.setter
        def ping(self, x: uavcan.primitive.String_1_0) -> None:
            if isinstance(x, uavcan.primitive.String_1_0):
                self._ping = x
            else:
                raise ValueError(f'ping: expected uavcan.primitive.String_1_0 got {type(x).__name__}')

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Serializer_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.pad_to_alignment(8)
            self.ping._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 2064, \
                'Bad serialization of voltbro.echo.echo_service.Request.1.0'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Deserializer_) -> echo_service_1_0.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "ping"
            _des_.pad_to_alignment(8)
            _f0_ = uavcan.primitive.String_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = echo_service_1_0.Request(
                ping=_f0_)
            _des_.pad_to_alignment(8)
            assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 2064, \
                'Bad deserialization of voltbro.echo.echo_service.Request.1.0'
            assert isinstance(self, echo_service_1_0.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'ping=%s' % self.ping,
            ])
            return f'voltbro.echo.echo_service.Request.1.0({_o_0_})'

        _EXTENT_BYTES_ = 258

        # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
        # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
        # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
        # is not dependent on PyDSDL.
        _MODEL_: _pydsdl_.StructureType = _restore_constant_(
            'ABzY8OyLG*0{`t=OKcn073KVCTaIbVAH`1Mv7^|uW7Blv#Ecy~N&^HcZjMXXNvbY_(U2VLO+%4W&QPEV7*G~1<YIsh;3*&=8!fdI'
            '(2bT_YN@4mRg1Pze}EQU2q;kWJ(Bt`viz5fCelKjdG~+r1<Av?W9sjI-<xRug(tnyl3yxkEZ?cQcG>-<T_`&lt5_ZOs=gaIak&3Z'
            'P^%Y%dd>NK)N|qo@wso}dvQ9{tcpF%<)=of<)BcjW}G5x{S&@M+@h1Y?fjzd_(2>dtr4f@yVXj}5~1;B`}#pl5+!~ee-nrMEISBl'
            'ZlNAHe*9IuRa$FGaj1RjI_1)OI(w~>9oSYNa%6JrkZIwux;;{~D;clm4!eOn;$(O^Ze=KD2HUe5o^^c{vsBxrJ3O&P@LJ6tjl*MK'
            '+WeHCeCAY!0`{>u?L=n3<&>RarxLWX*{Ybel;W`ai;C|KRh-g~D}giQ)H?m`vkGotm7C#WO7c>RwjWr-)e<lDba*ts>PVPnKH)M5'
            '5r;SNtN3;t9=80zu9WOrX``d@dLi7yJ$ZJ~4Mt-mr0`H%X5AIowz2GO<8qc#EX~f7Bz&@q!d$fqWj_wjtk$>gotGMX_dX80e&hx%'
            ')b8-xc735@RlPVgw{qf-4i~Crx5!a~GhF591$=mZ;yE=tsMgj|(ybzM`9!em;gL_Om7*Oum4~W|s)c6Fsqj%tbNvIi>gBRs8{MR-'
            'TO)S4?!>>1)0B$*0=v-$qmNr1yKPs7oZF7)1nyQTeQgcf4S_AU=x?4f63&v`Srfovx5C>bE}DAD&=7sCmu=yIB%zy#NN&F>%~w9Q'
            'aztwTOj|o6h17`j*1asQjSd-Uq(_u&+wIvTBZKEfd)Msw3BTX>P(9j1dn4*<$&w=0{w?)rA9Y3aN{3&5%Fhlw(uVfaD-osIF(Nwn'
            'SZzAM+eC*pMdA{E-u*=ObdU~3bhxFfa(S1qJ@Ul1)J=yYI{MHYxRlF|J(VvyLPsO&Sw))X^6FFD(=qCa==hd7aSbj%@l1Z{RXQHg'
            'YaMuTDfjpKGy9_x^jbu3JThOd#dS_TR}6Zc-iXLt!&YQ{>bX7ANirik-ST5TDt{6E%@-1nPSNRzdRJp^=z~D%trr%9-lX1$&OEj='
            '+`{DAT=(n?jZJUSnTXP>b+&tU?uEyovy_hL{1ey7Ex7*M+mZ*Jqw^76Snq8w_nF?<-;3K8m)@oe5oMkV2X4h}E^TX0bdfR<W!L8*'
            '-I|2U+a8rJQ8uD?o*EHu$?e|Vk^JZ~y%W)u%@cEh`_8UT&3ikR3%yHMB6|OsFyq$T_Uex2O7GG85#>6kD=X&fgB{O<u2L?dYtM`w'
            '_rUG1zm&Y`1G*N`hg;9#6&@oeX7R>L%a5+phY{U;E_}Hc?&G7ES_9pnn-TSGnpxicI;V_I!?P<*+TGMZLPkPGLg$==l1R!(s#wvG'
            ')G39OjFgI$PCe+6(W9bA$BIEFOc|yMQ>Qf2GSVv2I%ScSkyVk^DTkbloQj-Iedv?Xr=m}%e)P-eSJAIi9(fsg6?vToFd$<<#ehzO'
            '7?d%nVo)arCWEP9I(hJ9cq%-d8feI9sA%XkhA|mqD#mmg$GD7f72`TZh-5@6BAq5MA!9<tgie!~lrgDdQl}|Q$(T|xrPDN~WlXD>'
            ')@cSaGG<iF=roI28M7*8b(+JRj5!r^I?ZEV#=MGooffblV?o7&PK#KSv8ZBErzI@OSW>a1(=wK2EUQ@7X$31XRydv<T?q*V2@MGY'
            'NeM{>Ne;4sl!TOml!lan9tk}PdNlMHFeR7@Obw=iw1l*Rw1%{Stc0wBtcI+CoP?Z$oQ9l%J_&sa`ZV+z=$Fv1pkG73fxLvgg1m;j'
            'fdL5v3I;R`7#Nf=s9;dTpaCX<DPS6y0Z)Rbz|-IvXh>)%XlQ5{7?UujU`)f9fpH1r3dS{z8;B%C3L*`Wfe8r{3MMp67?_kWsbEsW'
            'q=6|3QwpXuOc|J#Fs)!(!?b}J2{Q_2G|U*7l`yMdR>Q1;ISF$L<}}P1n3piGU|z$#fdvT*3RV;>Xjm|?C}B~-qJ~8SOA?k8ENNIW'
            'uq<I&!Lo*B11nNgFF2gA|CCZ}0I4MV+5ZinP6{5i%cpmMPp4Wq?DFYt;M4rucnjSZ%BRi8eMWBspEf)D@V({J=K60SKNvnOYVPHp'
            ')1CeOLGx*WNqTh>cKP&o_;lyQ?DFZS<<qTqnKYNBcKP&k@afj4(k`Fg2|m64j@ahY>|1`kkwSCcjAU|^L(6Rrt#jfbn6x0#O){;%'
            'Od8GUGw0EQOsfy4(Skm=ne;A={=U-a7Ki3!`iW_@cv8)@P-{I34^^vFEyiIYt{3dEd&Ay_RTyopgxrhSAJ}m}+-H>>ujYs+@um2F'
            '_=<JcZ8#;%tJVU`EycIOgO*>d*NP4olpV{n0~UvdcqzMuINX!3`fejHP9MbSP`bopv#MA*kv%sKyNaV8v&$F7mVzILC%k&0>=vz>'
            'GgL2&i0k_xT&lO$K)BNlTNejft00-nnQTVv9>jszmgu&a?ek=6Vu7Q*$r9gZi{WoRHoy4%)7(X;QmmGolIb_C&FWn<a2i2o?;W>N'
            'bj*M`s}k2YYXShDd*b@GZ`x*Qltbhe&E_(Ruq}*o=q{LUAk-_>z^v5EyeOwO>{dh>8S^vuYsbvne$g(sJ!fKeg<Wl}6I|=qNjQ+V'
            'OC_$cX%~S@Z-z-;R#O~PvflaI2>bTdTBlX7xgfL1{>WR*{&X+?c|uAg*g>ED`9Ay0E%sOTw>0}Z`v?0c`&VeR*ME3(#O_ZV9_d&C'
            '>cE!$dt7*Zc=G>QyINuY-8#R_{{RLc=61d$000'
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
                     pong: None | uavcan.primitive.String_1_0 = None) -> None:
            """
            voltbro.echo.echo_service.Response.1.0
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param pong: uavcan.primitive.String.1.0 pong
            """
            self._pong: uavcan.primitive.String_1_0

            if pong is None:
                self.pong = uavcan.primitive.String_1_0()
            elif isinstance(pong, uavcan.primitive.String_1_0):
                self.pong = pong
            else:
                raise ValueError(f'pong: expected uavcan.primitive.String_1_0 '
                                 f'got {type(pong).__name__}')

        @property
        def pong(self) -> uavcan.primitive.String_1_0:
            """
            uavcan.primitive.String.1.0 pong
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._pong

        @pong.setter
        def pong(self, x: uavcan.primitive.String_1_0) -> None:
            if isinstance(x, uavcan.primitive.String_1_0):
                self._pong = x
            else:
                raise ValueError(f'pong: expected uavcan.primitive.String_1_0 got {type(x).__name__}')

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Serializer_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.pad_to_alignment(8)
            self.pong._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 2064, \
                'Bad serialization of voltbro.echo.echo_service.Response.1.0'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Deserializer_) -> echo_service_1_0.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f1_ holds the value of "pong"
            _des_.pad_to_alignment(8)
            _f1_ = uavcan.primitive.String_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = echo_service_1_0.Response(
                pong=_f1_)
            _des_.pad_to_alignment(8)
            assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 2064, \
                'Bad deserialization of voltbro.echo.echo_service.Response.1.0'
            assert isinstance(self, echo_service_1_0.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'pong=%s' % self.pong,
            ])
            return f'voltbro.echo.echo_service.Response.1.0({_o_0_})'

        _EXTENT_BYTES_ = 258

        # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
        # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
        # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
        # is not dependent on PyDSDL.
        _MODEL_: _pydsdl_.StructureType = _restore_constant_(
            'ABzY8OyLG*0{`t=OKcn073KVCTefM-AH`1MiKE!GW7Blv#Ec!gN&^HcZjMXXNvbY_(U2VLO+%3b&QPEV7*G~1<YIsh;3*&=8!ffe'
            'q6;mx)KW|BsuoG1{s1ky5Ky4#dnEN?Wce={O{9f5^X~uL3zCO($J9Uku{Y8D3r~5YCBIb8SiVzp?Xvr8yHIvAR<SzlRed*b;&A_+'
            'pjIyi^_uh9sOQ8F;&Wfe_u_P@SrvPj%TJF~%R!-5%{WEY`X_vixJ4&(+wr|>#pg;%Ys9JfZnYA#L}+}`zJ3ssM2X+VU&rA-%MOB?'
            'Tc`()AAcEdmDie59BQAqPPw$6&t9u!2euW6B$?bgWLkK<ZjTi0O2(_X!*1Y?I2m4#TN#R(!S<|%XI)>$EY-H@4o_|oyjHVE<M8+w'
            'Hb3PjpE{MHfPExRJE7TcIb~<qsRXTTwkl>Vr8w;VyyCk<6{qyGO5hARwN8Kgtb!X@<z~2;lDyQS?FZIywZuz39UjZCIud4?kGTv&'
            '#Nkc+CcYhqM=U?ED<!*D+URJ!UI_PaPo7<LgV7iXDLmYkS$74tZ7h4+xSXXFOSAJN37_nuFjuWY*^k3BtM#pW=cNYUzmLPNpSnQ{'
            'wLAQ_U0<kJRWA<Bt(^Fy!-Z<uEpn9L3|BdN0Uw^9drr*`s<m~LbgRf*J`wDCc=Y3HrDz9E<)NygYN1(kDty$^T>s#$dbw=ZMmK5d'
            ')`(rMJMr)1G^HZHz;3j`=;Kz$Z`+k2=eFZHfxA^oUs=O;Ltx7-`kSYWgtH`f)&y|at?)L9i>6*OG(=zPWm`BPN$4gblH0FJ^OcXS'
            '9Ff{S)7H*NAvGesbuWu+qeDg-=@BK{c6&C-$l!U=-ZguE!teJzRFC%1-iW$dvZRQ$e@i{uM_mye=<v%=`Psoo+R%PF5K*cfBcel('
            ')uw~IO>}ruBrf6S-A`mshv;xbM_Rfnmv;%<qfcy0-E<_PV-L-NOS$a$Q~9E!bS$EtRit??uROIq9jBg%PHdSI*WmJ#&*Yb0p%W3k'
            '+JP6Ba(}Nqvp+gXuSWFxBlG22T<6qt#h};d^@z+hY(>^@Jhw+WMP@{&TYk((<u9VY`9k8+8+1CN-qn~J`XEqx>xIRjH>o$GGmq^I'
            'w=lUj*FF0}W7Au7CZhCeo$a2Td*LzYETtnl|HO523$Fk6w&X$Q=zK&M)_dE_eWo||_u{t2rMKxqM46|;fm?B#OWT?gU8GDz+4VU{'
            'w<h88wnwE)l#S?}r$&TZa=UkTBtN=L??iNE^Tb@>zO$=S^WKi-LhsU*h~9rD%(ykTy}F~h(tGrNM7hrC%8L2=V8`>ItCWlA+B0Lv'
            'J#hQ$FC}mKfUZUK;ns6_g~!N=S-kPm@}ukYVMI5d3t#Sq`}oOAt$}XP&4~Io%`ESJol{1q;n|fY?QUuyAtRw8p>xhbNhD<?Rjg=8'
            '>XbrCMoL9Wrylgk=uy$5W5pm7rVLYssZ$zh8EF-1owCTv$g0TdltWHNPDM_qKJ>}xQ_-hWKl)|#tLWD$kGzb$io8w(7?3fbVnC-s'
            '49XZ(F{l#*lfhIlojiClJQbc!4K!plR5WxN!<dXQ6=OP$V_e3#igBGHL^2{3kxmnskTIcRLZ?Yg%9vC!snZmuWK5};(rFsgGNx5b'
            '>okKI88a$obehGij9C@4I?Z8D#+-^do#rtwV_wC)P77F&v7ll>r$sEvSX8m7(-M|sEU8%1X&K8hmQ^h4w1O2GD;!Ubu7rewgocEH'
            'q=ck`BnR0*N<vCON<+#(kAxltJsNrpm=a6{rUuhMT0&YuT0`1ERzg-mRzuc6PC`yWPD9Q>pM*XIeH!`<^h@Yh(66E2Kwd&#L0&`N'
            'z<`7S1p^ue3=B#bR4}Mv&;XOb6fh0UfG5FI;A!v-G$b?>G&D2}j7b<%Fs5P5z_^5Q1>+jV4MY+m1(Alxz=VVe1rr)33`|OxR4}Pw'
            '(!i92DFss+rVLC=m{u^YVcNiqgc$`h8fFa4N|;qJt6|o_oP;?Aa~kFh%uAS8Ft1_Wz=DJY1uF^`G%Ofcl(48^QNyBvB?(IkmNYCG'
            'SeCG?U|GYmffXsL7aUI5e?ciWfK-zG^8bcUCk2n%<<mRBr&BE)cKP%+@M->SyoK%y<<sWlKBKpRPn(^6_`&jNbNx4v9}S-tHTQDQ'
            '>CXQCsQI+OB)vKbyL|e4e7bXDcKP(v^6A#QOq$D5yL|dN_;l-2X_rs$1fO1iM{M(H_6<MYNTE4zMl!j|q2)G*);aMIOj?lWCYe@W'
            'CXMFwne%8trqzejXhEObOnR3_|4?aki$ilV{lqj{JgH_{sI?x2hpJVo7UM7x*9&&oy<u;|DvY*vLhi-vPwa#r?z2jcS98RZ_)>g7'
            'JYd~*8&1jcs<ps!OYyDnkmXnFwW7lXWykXDfW@I9UdnDE4)^4%zT3!)(+6=nlrHhutSWX+WY3MmuHvZ2?D9pirQpZmNv~cgyG5(!'
            '4Asjb;`%-am+GxG5bkut*2TfrDoEyXCYuqv2XP>_CAuwU`#hPNSm0={vc&h<V)(m{%+EjjBzMuN6ssktWcp2OvwGJIoJNq@d&jL5'
            '9W!9gs>JopngGD(p18j4o3>dR<q)|=v$;$nYzw0tx(lWo2=z)eFe~*kFUqM6yA@GJ#{AU%$}#h{U$o0@&zYEAVOLx01lKxt5)S6='
            'Qi*G9+C|{fn_-fd)fC5+tatu4!oIn+)@jwNiUpZP_GjK=_LqC{uM$!s!4CQC+xzUhTkNmwZ)x^-_7C<?_OH-r@Bi@Th~=L+Jle4X'
            ')PXJg_qg!-@Z|rqcD2I(yLEn<{{b*mY!AOA000'
        )
        assert isinstance(_MODEL_, _pydsdl_.StructureType)

    def __repr__(self) -> str:
        return 'voltbro.echo.echo_service.1.0()'


    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8OyLG*0{`t=No*VE73S=;ywUL{$4NX%9GiA*TG{2SN`eL|UOtzwlR$^Mqaiu=KMF;%!=XVHFrXY-$i)C1AX7j`9d*=EM;&$4'
        'QAZt`R&9Y+?MXcp==(`(p=Ehr&_p~8Ise<g_dxO^-?;wA#;H{65uK=wmFlH(&Z&EW@0R`FxP`KpbBfi`TD9(nUJ~uT;srPSqW9HU'
        '%}c&d&U}~LOtR5lC-8pV@amxx%5#y5_Ff5tMloyzw`m$q#T{ioFW;z^!$MHac}3B_$e7Y|?sD5z5~ZCRUQqX|73t9Wrt|vygcM5s'
        'F8Pj=aojKr{6Zu2>dDn)yY$zUlF0bN_sXS>bb6eU8@ipWt@feliH<hh8%4L0s|Eh3ANn`E9GBx)t|wxT*tZs59Jrc@!yTL6==e6l'
        'gTNh2qNCrqe99+ZdX?*;_*9<Wj-glfM!iZ0!|jS$PbrBGeqE{i*DGG>=ataA?giccb~^<>bjq!838lHzqRR~$t(Lgd)6tRqnj>kJ'
        '`<!KvB8E5h+vIW*9dhcSTPe9gX|tn=Mj_h8o@#E<562Rul<2vR%(*79?O=JPgUdO}i1XqCDblBSQ=02ep<GX*Q)~5Yc;`~X+wYTT'
        '&u4zvM(qmUcIt~Xr&>!QdpjrfvC%@c>=zj&c%xNDFXZ9*Ma>J`uo`TjWI9FR^F)Y&=<w&&O3@9y${kf@)lxI?Dm-dg*57}rQ7*f|'
        '*cMIGx#5-@Uh;<|OPRP{5TA9x_!(Orz3f)5dzZbM7y8?!^sO`MHYK)ff!3+WOJ`|z)&g+UuW*~>i<VwGvSeQyWmh^NMe3$vQajID'
        '>zT(^jY;pE8S7`Hksg!TzE|aIt4l@(nK7k1cDuI7$l|=HXWgDp_<r{t^=KFM#I&a^OUqb$x7DNFv?r#0U4HqL&-UNdhW66Fm@=Ih'
        'F&((4Htpv&(Q{iOv4qbL-j_Wcpyy&b)YjEmzDL>~zHeJPNQYuNa>pE4%Ce&m<cki|k(hedkmg*DJ+M6;rQVpH-!>=KVEOTf@=M3)'
        '`Iuhl!i%Ns@5P7qN5|=fm|nVTzO2PMCmtyVy+|*`WUpf@vwr!JJ<<uXV|u0S$G%(sGWx5JB_6#@uf%k6E#{^^NR(cCY%%CnIvLZc'
        'dv=B`Y}RJo(~mVay+)^E%C6Pf>Digb9)nI(Hm0-pT_;<x{_9U94?06<V>-9d+mq}wyScyTpIBUaozBISdmtRxift}D(VXZ!<znjF'
        'n1gJ465e>?QRxEp#q{O_Bf^$!_tsO%kKUj+V|sh*#PF9mmUgD*ou`%yy+v=w^zK7p#@1~6-c!w$-l2D6>hGSeJ~>|(pL!nj9`(oc'
        '{zGHO9@zeaXOcHvr1xX`aQiuYn`89LS^Vgk<wqaThcSKpNcgfB_VLLxt${wGk7F9xGPB(M22)0_S#v8b+TGGXN<~UX%4E(#X{1%8'
        'b*vglo0LIDMMg))q+ax@=+)6{V$~uWwhCK^ZBiCl6<Hlwllsu7qEAPkN&V<o(XXT5qyY@57|=0b(jW#^4C)v(DUZC0ypFs{Ll{yq'
        'q+`gWVGOGn)-i07fKVZH2$O24si^6wnbbs6MN>!9q;ZU^7}qgw(gY?{Oz4;}DMqX!))AXDiAfccIwnn;!jy_B9aAPvV_L<uj%kx-'
        'Fr#8d$Bap{m{l>WW7ecO%&C~uF=x^|=2gt=m^Wzw3n~_LESR*2MHP!W7EM~hl8PlAOC~L2S;exBWs_F0qGCnIib<<jRk6x=GP(*<'
        '8d3&Q7SamR8qy51g^YrXhKzxXg<b`{8hQ=%TCf$^8f*i$g{*?ChOB|Cg+2v+8u|?MS?E{Luc6;Szl8w>0~!Vl3|JUcFsNbBz@UY^'
        'g1m;jfxLww1w$H!3=CNqRxqq#*uby_p+IO5284y0f|`b!ftrP;f~JP1fu@CV1>+jV4UAiuP%xok!oY-uSV62IHV|8wR4}Pw(!ivJ'
        'DFss+rVLD3m{u^YVcNj7g&74i8fFa4SeR8Xt6|o_tc5uRa~kFh%vqRMFt1_Wz`TV81q&J$3@lh!RIsRFRl}lzMGH#`mNYCGShBFJ'
        'U|GYmfn^IT3RX0%7+A5es>F?g$AtZtlo3~vNsC|o-|*?Q<WW0(`YG_~OdE$CKK%svG=Cd!qx)F-w0*D7=qJFZ?e0GOX!*3g@f*lb'
        'hEL0yPqOE1cYlA<d|G0XU7Lg*K7AXX?w*((KK-D4y8SMbWm#s2Pd@^mZhtE6@ad<)r#IdaJA7J9@$qH~&Ab`u^csg&I~>|%;vt!|'
        'B+)H0tv^c|&Geahv?SB|ooTeB&mAVcL!*DJG`h{9nM~g|jh6pZi=N16{}mqTPN`Z<qEyl-xY5B)dmBz+ti2L)GZB9hC+g8|r{vWF'
        'PyQ2MN^V8_oNIp5D>=1l5ITM-xfC66>eWV2^jJ{#oSGYoB(mgF*)Jr~u6(ubH}mrJ`y?AF7dW=4%9Rtf<|omf;#f_%<@0h&p`Jv?'
        'YmGwLFFJvDy-}7CH}*kTYPQ!v*y*ONi~a3YklY)&zMR}WNJ6<SanKQNos$XV0!L?)CAlSjh<^X6{q<L0^q==C#cIhb+4YvSUA<<9'
        'UNg+~T=6SK&klvRCh_ZbAOWbeC)RiCwriKh7$U!Dx0XqyZDEX|J7@c$RIgM+yV59gQC=|WS7aGE`%C{@&(6E`qFe5G&L!fa_^`cB'
        '@JZKB!v4HlDzV0vT?CeX9;LagmN=nwqx-iJF?DIZ(|WD7AoGLxGq+g$<z_NsD5;b<QWt-{CH{6v{9XJbEB+}~#J|M9BdfFi!_ASq'
        'KS^}BYXztaTk)R>>Gh7ukEA%pdanN+(fD@zEP0q1*IKnw_qMG3ymGgNq_&OR{>gN2{fJ|&%B#0k{ye8K(#w}S6+dE0X<A-(@#XQB'
        '$mty0wvzP%vYRSMvx(JN-|7^xAssm+d)O1DgLMpA8lEgOJ90)Aaavx^$;(;3H14<JTWwFd{{cs$F=~J&000'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)