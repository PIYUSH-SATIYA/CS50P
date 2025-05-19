from plates import is_valid

def test_firstTwo():
    assert is_valid("5050") == False
    assert is_valid("CS50") == True

def test_number():
    assert is_valid("CS505050") == False
    assert is_valid("C") == False
    assert is_valid("CS04") == False
    assert is_valid ("CS50") == True

def test_place():
    assert is_valid("CS50P") == False
    assert is_valid("CS50") == True

def test_special():
    assert is_valid("CS,50") == False
    assert is_valid("CS50") == True
