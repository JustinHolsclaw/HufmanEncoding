from huf import HufCodec

def test_huf0():
    huf = HufCodec(dict(
        o=5.9,
    ))
    # please have the lowest frequency node be on the left (i.e. 0 bit)
    assert huf.to_dict() == {
        'o': '0',
    }
    assert ''.join(huf.encode('ooo')) == '000'
    assert ''.join(huf.decode('000')) == 'ooo'


def test_huf1():
    huf = HufCodec(dict(
        a=6.8,
        o=5.9,
    ))
    # please have the lowest frequency node be on the left (i.e. 0 bit)
    assert huf.to_dict() == {
        'o': '0',
        'a': '1',
    }
    assert ''.join(huf.encode('oaaoo')) == '01100'
    assert ''.join(huf.decode('01100')) == 'oaaoo'


def test_huf2():
    huf = HufCodec(dict(
        o=5.9,  # ao: 12.7
        a=6.8,
        t=7.7,  # et: 17.9
        e=10.2,
        _=18.3,
    ))
    # please have the lowest frequency node be on the left (i.e. 0 bit)
    assert huf.to_dict() == {
        '_': '0',
        'o': '100',
        'a': '101',
        't': '110',
        'e': '111'
    }
    assert ''.join(huf.encode('ate_oat_too')
                   ) == '10111011101001011100110100100'
    assert ''.join(huf.decode('10111011101001011100110100100')
                   ) == 'ate_oat_too'


def test_huf3():
    huf = HufCodec(dict(
        _=18.3,  # _hse: 38.5  # all:
        h=4.9,  # hs: 10.0  # hse: 20.2
        s=5.1,
        e=10.2,
        n=5.5,  # ni: 11.3  # niocl: 23.2  # niocladfwtmur: 54.2
        i=5.8,
        o=5.9,  # ocl: 11.9
        c=2.6,  # cl: 6.0
        l=3.4,
        a=6.8,  # adfw: 14  # adfwtmur: 31from huf import HufCodec
    ))
def test_huf0():
    huf=HufCodec(dict(
        o=5.9,
    ))
    # please have the lowest frequency node be on the left (i.e. 0 bit)
    assert huf.to_dict() == {
        'o': '0',
    }
    assert ''.join(huf.encode('ooo')) == '000'
    assert ''.join(huf.decode('000')) == 'ooo'

def test_huf1():
    huf=HufCodec(dict(
        a=6.8,
        o=5.9,
    ))
    # please have the lowest frequency node be on the left (i.e. 0 bit)
    assert huf.to_dict() == {
        'o': '0',
        'a': '1',
    }
    assert ''.join(huf.encode('oaaoo')) == '01100'
    assert ''.join(huf.decode('01100')) == 'oaaoo'
def test_huf2():
    huf=HufCodec(dict(
        o=5.9,  # ao: 12.7
        a=6.8,
        t=7.7,  # et: 17.9
        e=10.2,
        _=18.3,
    ))
    # please have the lowest frequency node be on the left (i.e. 0 bit)
    assert huf.to_dict() == {
        '_': '0',
        'o': '100',
        'a': '101',
        't': '110',
        'e': '111'
    }
    assert ''.join(huf.encode('ate_oat_too')
                   ) == '10111011101001011100110100100'
    assert ''.join(huf.decode('10111011101001011100110100100')
                   ) == 'ate_oat_too'
def test_huf3():
    huf=HufCodec(dict(
        _=18.3,  # _hse: 38.5  # all:
        h=4.9,  # hs: 10.0  # hse: 20.2
        s=5.1,
        e=10.2,
        n=5.5,  # ni: 11.3  # niocl: 23.2  # niocladfwtmur: 54.2
        i=5.8,
        o=5.9,  # ocl: 11.9
        c=2.6,  # cl: 6.0
        l=3.4,
        a=6.8,  # adfw: 14  # adfwtmur: 31
        d=3.5,  # dfw: 7.2
        f=1.8,  # fw: 3.7
        w=1.9,
        t=7.7,  # tmur: 17.0
        m=2.1,  # mu: 4.5  # mur: 9.3
        u=2.4,
        r=4.8,
    ))
    # please have the lowest frequency node be on the left (i.e. 0 bit)
    assert huf.to_dict() == dict(
        _='00',  # _hse: 38.5  # all:
        h='0100',  # hs: 10.0  # hse: 20.2
        s='0101',
        e='011',
        n='1000',  # ni: 11.3  # niocl: 23.2  # niocladfwtmur: 54.2
        i='1001',
        o='1010',  # ocl: 11.9
        c='10110',  # cl: 6.0
        l='10111',
        a='1100',  # adfw: 14  # adfwtmur: 31
        d='11010',  # dfw: 7.2
        f='110110',  # fw: 3.7
        w='110111',
        t='1110',  # tmur: 17.0
        m='111100',  # mu: 4.5  # mur: 9.3
        u='111101',
        r='11111',
    )
    assert ''.join(huf.encode('what_is_this')) =='1101110100110011100010010101001110010010010101'
    assert ''.join(huf.decode('1101110100110011100010010101001110010010010101')) == 'what_is_this'
