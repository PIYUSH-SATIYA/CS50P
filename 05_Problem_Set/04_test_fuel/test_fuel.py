import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/4") == 25
    assert convert ("3/5") == 60

    with pytest.raises(ValueError):
        convert("cat/dog")

    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
