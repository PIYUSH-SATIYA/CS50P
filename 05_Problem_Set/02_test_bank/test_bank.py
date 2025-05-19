from bank import value

def test_0():
    assert value("hello, this is me") == 0
    assert value("Hello, This Is Me") == 0

def test_20():
    assert value("hi, this is this") == 20
    assert value("HI, THIS IS THIS") == 20

def test_100():
    assert value("lorem ipsum") == 100
    assert value("LOREM IPSUM") == 100
