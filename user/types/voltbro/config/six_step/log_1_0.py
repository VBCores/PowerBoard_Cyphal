# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/cyphal-types/voltbro/config/six_step/log.1.0.dsdl
#
# Generated at:  2024-03-29 15:42:04.199040 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     voltbro.config.six_step.log
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
class log_1_0:
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
        def __init__(self) -> None:
            """
            voltbro.config.six_step.log.Request.1.0
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            """
            pass

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Serializer_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.pad_to_alignment(8)
            assert 0 <= (_ser_.current_bit_length - _base_offset_) <= 0, \
                'Bad serialization of voltbro.config.six_step.log.Request.1.0'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Deserializer_) -> log_1_0.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            self = log_1_0.Request(
                    )
            _des_.pad_to_alignment(8)
            assert 0 <= (_des_.consumed_bit_length - _base_offset_) <= 0, \
                'Bad deserialization of voltbro.config.six_step.log.Request.1.0'
            assert isinstance(self, log_1_0.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
            ])
            return f'voltbro.config.six_step.log.Request.1.0({_o_0_})'

        _EXTENT_BYTES_ = 0

        # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
        # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
        # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
        # is not dependent on PyDSDL.
        _MODEL_: _pydsdl_.StructureType = _restore_constant_(
            'ABzY8OyLG*0{?ZAZ)+4W5XQIl?A8BBKY)TDRdB0c!MCU9(TeXRB%A4NAiIgl<hU&q?3+>{pm^i=b#iw_skm=;W@j=_e$VXJ(XXGo'
            ')%wX#{Gg+@wTKXmwB}4I3$<um=Up@ilpma6NDZa{9|sS#q8Ar*PKWun=w-+CXA5Uh1y?t&KQ;3@nx%*czP4^&AH$af5h?GB1%zl^'
            'Pi>XQpSJOeCOebrk}fFU6B02Pl@KC*rhM>MF4V9QJ1>12e1JwGX!@2Pic_-$ExZdTjHYRRETT)H0WMe&USdmmTwc~F%6DdrwVai&'
            'D~8xPqC9F{;n?+t^8IG;t+cO@Q6rz*vQggK&@sq0A2%1mH}&hfI7mpx<<_l?EE=H4V(G#(Kv#Jrv}-6=EGCrY!OyR4R|bWJevU1-'
            '<IS8k-Wq(j&QCbqnxAh8$NEqIHzW?7a@Mfo!F%W&FBRGC4<3R<7yhhpPc*Hun%bB7(M)P>`uRUi?NO;tleIDoH>*5hA#DQsPKT4~'
            'M^wCLzZpc6{iGPTGd)eJ63Ar<#-ejNSy@is6|nTOU;hfzq@qfy{taW8j-Q<Z000'
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
            voltbro.config.six_step.log.Response.1.0
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
                'Bad serialization of voltbro.config.six_step.log.Response.1.0'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Deserializer_) -> log_1_0.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "log_item"
            _des_.pad_to_alignment(8)
            # Delimited deserialization of voltbro.config.six_step.log_item.1.0, extent 560
            _dh_ = _des_.fetch_aligned_u32()  # Read the delimiter header.
            if _dh_ * 8 > _des_.remaining_bit_length:
                raise _des_.FormatError(f'Delimiter header specifies {_dh_ * 8} bits, '
                                        f'but the remaining length is only {_des_.remaining_bit_length} bits')
            _nested_ = _des_.fork_bytes(_dh_)
            _des_.skip_bits(_dh_ * 8)
            _f0_ = voltbro.config.six_step.log_item_1_0._deserialize_(_nested_)
            del _nested_
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = log_1_0.Response(
                log_item=_f0_)
            _des_.pad_to_alignment(8)
            assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 592, \
                'Bad deserialization of voltbro.config.six_step.log.Response.1.0'
            assert isinstance(self, log_1_0.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'log_item=%s' % self.log_item,
            ])
            return f'voltbro.config.six_step.log.Response.1.0({_o_0_})'

        _EXTENT_BYTES_ = 74

        # The big, scary blog of opaque data below contains a serialized PyDSDL object with the metadata of the
        # DSDL type this class is generated from. It is needed for reflection and runtime introspection.
        # Eventually we should replace this with ad-hoc constants such that no blob is needed and the generated code
        # is not dependent on PyDSDL.
        _MODEL_: _pydsdl_.StructureType = _restore_constant_(
            'ABzY8OyLG*0{`t;U5wmT6`oC+>~6A6Hr=KmRgftlnl$ay|Gq9rY?F4YYP#FihJ*?ftULD291kAb^3Q4)RFoot5@f-O+*aic9{R>Z'
            '9;iT6AS9});wf)D_K^zF()UUg=Z-xy-to?)Y6Rkem1b?9bMCq4@B4gbuHX0S&sG|Pzx+(J>n5(>vJ)12)c3wmJ3edKPS}sa#7h~^'
            '@4uABnUiKQ`{r)M_$_|!75*|mn;)?Q+DH9YwnIPd#9_+`gKJ*5m3TXLlCr4fhuzi|OQJAH&}_lpW^v+$0f$CDf2F*?#oKf3#!vVw'
            'JU?#JG>yGZma>Fj<<lY?8S(tcn#X*19MLh`r75*j5hiYO|1-?@`j~^eKk%cr7X&QkaHtT#k-Rx02OB-~In2Z2FjQE&imR5()hks$'
            '8Qpeh(28QQvA4}yi9>xFx1JAD)@3oN`5C*Jmhi|I&re<Qx&d=bXZy1{Zg;%Y_F2$Pfwvd17!FNRyC1q(jC1)zn?pBZS?eO|)`bci'
            '(D*Um;`xJ^Fb!N9yH!UwvJR$oWSjaK?th={h7QjgJnPVWrP43Evs+BV%N%rgG{I<G7RAh=SbcsoKVe_<c9?5NVVv5Y%Qx~<b`oZ>'
            '!%*QfJEFK(J})l5*Wvl%CJx`urjXvk+~%Idy&)9Sb|~_AzU1siK>a5~rxTt(9AzEfbL^OPGhggDo&(e#Eqa1ZE0sK2^aV>g>`Y5;'
            'Ni9)-o{Dm;*gzAED`r6|8nW#<jNb$UOsqo3N55YkwrgB2G)yO-G1?1W`oiG(5<Zp<%MaUO#PjAfC&_NV6Jk;r$vW$YI1DM`<;94_'
            'G!5hGFgxHO2;fqFa+A8Q7j$bz@RHDOWIkrRJE=tvMR$MB&$bu#k`5v@DjeY$WgSen?*(F_@P_V)n|U!+SZT5Pn9X(~8Vta^k#&+z'
            'F)&_Y3#4PY@Og}sM^JYhbvSCiFLtO|jIs2^X;|7~)K`@mNWyVnT=PSk?n4N)+D&*8RM2i<)P33wyfi}u<crs0>WJ!MQy13Cdt8=3'
            's%nx#6jd_}mFNl~x<zE!lr)*B8qsvwuoPX>BrX6{1qv9s@$3#d@^_oDz(ImjB+%USifK!pYJTSl*)UC0k&VZj=ZCjf1+su3ihcxH'
            '0#Dt9uWi8B;TvaR6`qC*a1ow?XJHMV%TE?n*gv(<9!w~_051-5hAp@}8i8+*?!H?nspxnUI}VO$G`LtFhM#MwgK;mHQW|#|f*@ju'
            '<yyl+k@gJTG3GPJPJyL#R<|Fy3v<qH`1x9k_qRiATh#Rp`1Q=XJ}}zvzfju4o8MYLxN3)=x1XM>xiD38v938?-hIAO>@Q7w-9?^@'
            'EGk&~Q@-$Kg4EDv^=xO<v(>U^@B{eaOZr@+A)A(ISgMRDGZa<UO^L{wu9%vlnyLVxsvD+7BvZnxuINP5EXzQ2TC%B`29d-X#gI%Q'
            'A%Jz2n1-YiOV^2^DyCr&lgOs5Ymz3UsxE6PQ8WYHYpNovib05lk1|1HqTv?!kyKqZ1>}h#;cl{|n})8-$PbcfD4MQWl4MCLu~Y>Y'
            'Ym$kZ5nV!>&}CJ%(6`u4Ra6756h*N#A{#o9h^|{I?y9JmEvAU66U9)FWHimh<S|$kqcvqBS+b>A79p~tOBlPP7&6ghMI-3fAP2FK'
            'baxg~9(znzk%9)-G5`Dx?%bV!4DFslvRVbnDuQHn5+o-E(Z<xbSsdegt2W_(MWdq$o{XqpDw#;(Ec_kbg@3^N*#UXv^CblE{a1hh'
            'xqk=)eCLjV@R>5aTzT=Hz8D7L926Y*2G19Z7dW0XxB%Hf-rgG)Xk%Y};60X<!s}yU#q|0_DdBB|<2wbI--Y+@UM2V^d;lN9zbcvI'
            '%b)FFGAVCg&mY25UU9^ZZD7>JOL6!<m#<t7lBtK)lBebNoS4~ytq-i|$A#z<5pj)Lt403Y77e;=i$yH;rX7^NSDas#Cnivwc?Q$h'
            '7?!NPAmoj`WKg?7kq7+!tGcqB(UaTE4;?Sv9kJ)+kp5XrvXjMw^W;9GvJD=b0Uvts3+ThEa0_0C*WkDCOZXkU34eg!!yn<T-g)Fk'
            '_*1Wim)_&}Z+g%2Q^RjA_c*`R4*cKpf64O7h&C5+HW$VWaHW{oWt1-0cwtif)52InsZ=+f5SPZADBY|ZPl!w72&GZoctZS}!gvp*'
            'dv)Upaq0OsN^jSVC&Z=k9hBaw8&8N!<Bw4KQQdgIxOW;6IIv$|o&&bNH&<IxQ&iSSLM0ulubEVo-2E_e_ZJH8K7%yTM~Zk2>ETVJ'
            'hPRLt1ReZGn4~A6x<Vbj<M@p6^_Ili6Zo&n>AeSp<9j9aUUTHO_hr0oug&1>vQ|?_dwuiJRMuV?|GG2&hS2+q$lz2mom!W~4_gzg'
            'dgD{DYVWr2T=_y!#x@G6^>0UZS*)28000'
        )
        assert isinstance(_MODEL_, _pydsdl_.StructureType)

    def __repr__(self) -> str:
        return 'voltbro.config.six_step.log.1.0()'


    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8OyLG*0{`t;U5F%C74F%enc1K0&N}V}TunNEn{nfI>c4J9#MvJQLuV%AY&6QU6xCgK`&6a6s!~70jAUU0MrWnKfxQuY5Pb1b'
        '*`SX;<So9rL<~wEM1mj&A^4al&+V%2uI}pYjcyPG2d3-ZbIv{Yo^!r)?y0(U=*^p_YrVhh(Qwy}ZLeX*G;%D@`L5OSXv1s=-7tuq'
        'gtF||RT^zOZTiw~NZB3s#n;(Qwvs($M)cK`#)+A5I@Gd<t|n31PSR*h^04V!UDWf$cHkwgC}^|;|Ay0P#LkWxCp2t$L8q~mD`VNB'
        'xlN<k34E?{;akP{4r|UeYu{(D<8e$YNg}6}CNyT(S+-o7o2}h^vzuJbreQ?eRzhudJ3C?CaCWF|hC!5=j?Ff*Q)V2bQJW&eqh@F&'
        'z_JDY@SGOQj%=d&JDZ$(2aT9}mSu+^;C37c9hMz$?}lJ`7r5~;t}AR~*?evt8q&89g}H@dLuhbMvxIH&Q-c-brV;fM?t1QEwwE0;'
        '?V!!F8g6E`JXCzHAD)(zm>%^z37~i~KF2*SImrvX`Bj`2&d&~-0q$R)rX=3&wgS(=9hcW>H^AU0=<OFn8d*sY4MR9@w!!gi2G3?E'
        'H!a(C{7yv(6wcj9J<p1E$GNCs+wxM%e#BOqwf(q-aSn4utht!B(A=)$vu2GCtQ|gBFuQ@BdKO=O)TBG1<@cblk+$L%t~h}JjKjc>'
        'X@S6n;v7e_CubuqU&Y`!EWs&6(3BJyz=~yu*BpxG5Bzb|w5`M%BL52YoGvDdJ&OE!)A4;8m5)}RaWoS(bosGP^uf-Lw*oH|t6wbZ'
        'Nv-X+<u}5JZ|rQ-M%=d0^Nr{Igm!2|Dtd-$rWriY#j;aZosLiKLfNQQ$4W55;Gr|x7M1~w7CM7wXEyt4__D@j<gIfSrf}^I4*k!f'
        '!Ip1ZkzH1_m$uNX!#PUe96X)2ELgtD;8keHaQZf!*?@=Pb1QHbJ`Z1jN3yeF+Cu0e3Oa}q^!+d<m^bsee=v_rR?X)=Li74w8qG?0'
        '>NejQR^XYQt<V5*0B&tCdM;;vg=2XUu?%135Qf#}B3#7(OUS!Ypp={B#3rw1J(EhYypFtM$U|p%9?ye{#4y^AOpEpwwLDpx5o-*{'
        'ku@){l93pK+pNPY5J0$x;p<u*-$_!8QFi1;WVLw>Ko>5q6=PhMJuNGOL?l_!G?}OpA*w+{Q5O`E$O=(ZQ8Oe}Q3S?AJQ~VO``QjF'
        '@^<SHFUT=gJdU@zlgA)_u72%;sOh>ciQ1Ry&-91aSswvEh5bngfEW@;VLLmSd*Oj&Sue-3j<Kwd$MSe$MIDL-JEVB2R08%xZuSh`'
        'QR>mQnE*|!S<!y%KDj+R;GIf{r)AdL@SB-_{mfv$|AK1|Zoa%e*=q-%H!n`*T$;+cT;+VD7`;?-_T$qEa_HDtTX?(h2}|<KB-NBz'
        'F}pK}*=i9p_%ZzC+v;4cChCT+8M263rb)7>>H-lJRniqn)@7c6va0C@5p)5cs-zM{F$@i}(-3t<*NDK^NSdG%0TWo2iLMDMF;tak'
        'vZQMo(TS*wsv;<yDyyO*6G_ofy&_AZENO%oI28#B69u=xe?eAdou@p}1l&y&R9#b55$l7XYm%ZWh9DS%Obl7V#fqTgW<(XROsJwP'
        '8>pM_CQGu0Qj#PY3K2Dx2t-v48F!Urv=&W7(}|=>SY#AMN8|CZGM-i!iC~C^WEg~qk}BZY1xXW$B1#HDy&9QRg@pT8A?f^iRmKw3'
        'dk*W*KjFjs*B?!J;3QcsC&?-%$?ABLoami4vOJSU5q4J<g#Q(V=3~6OEw5lwZo-Ot0HFjQxQFrK9>kw?l0lC`9UjY;hsghrOcG1|'
        ';OWbO&pU8`Vq=*d$@@xdf*H@MN!mW{dt_t8A@DJc3*xOIu_StH%y;l-%)h_n+517y1^>2Z+y!Kp9Dyw=-9g(D*1VOS!Pkwv35-mj'
        'mW_|RJ*3(4H~n~OJ5|)_ZgY-fHm}x`9PBRR=Dmq~21neCN`WnV{^2dl@6at8(!`n8)W4GV+Dj99njQvgeLprAi@v?*(4OaeRs3gF'
        'W`Wd`+tdr%PO>|wq2o|}pX0fmM!h$n5urRV@IAN&KY%yj7qAC+;g|3$cnf|9zlL|=9{d4*4}XOB+{-+8e{$D&@UF~;^{IY`{a~P;'
        '5QqQE|L@DcHl>M&*K)KkA$6%zXvWDu&xHk~3RU4Tav{8l)Xl2!7`YG*ks4No$H?#G!uv?wuL_Tm3(a?tdbcV(MlOW!A@yEWc#K>K'
        'e}vSJs=}jW_X4lTTz-9N4lb_m&sA1b7^O7=X9)+YYsMMHW$-dy2H(jqgKJn~_OQIXg{9>lmX-Igo?IDR51(=sa=$)$g}6`P9M9)I'
        '$=9CiL$$aS-1A)Vr*kE^WT4#rG7g(-Gpc^!u_<MLee=N7y1zL5jxl`GaNp;4tjAN`0*~iD+4}^g*!?Y6R(h8xj#ECx*%@D12H$<k'
        'UHl?0S|~nfR<EixZdf$<ZdC58{?6m}H~#Yv{`29?==aUMovUd43m-z=l!z4o00'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)