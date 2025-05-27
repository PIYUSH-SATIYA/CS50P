import pytest
from working import convert

def test_valid_times():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:01 AM to 1:59 PM") == "00:01 to 13:59"
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"
    assert convert("12:30 PM to 12:45 AM") == "12:30 to 00:45"


def test_invalid_times(invalid_input):
    with pytest.raises(ValueError):
        convert(invalid_input)
