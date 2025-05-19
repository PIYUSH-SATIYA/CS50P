from twttr import shorten

def test_str():
    assert shorten("piyush") == "pysh"
    assert shorten("hello") == "hll"
    assert shorten("hello_World") == "hll_Wrld"
    assert shorten("PIYUSH") == "PYSH"
    assert shorten ("HELLO") == "HLL"
    assert shorten("this is CS50") == "ths s CS50"
    assert shorten ("Hello, David") == "Hll, Dvd"
