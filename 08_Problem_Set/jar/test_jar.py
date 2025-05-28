from jar import Jar
import pytest


def test_init():
    j = Jar()
    assert j.capacity == 12
    assert j.size == 0

    j2 = Jar(20)
    assert j2.capacity == 20
    assert j2.size == 0

    with pytest.raises(ValueError):
        Jar(-1)


def test_str():
    j = Jar()
    assert str(j) == ""
    j.deposit(2)
    assert str(j) == "🍪🍪"
    j.withdraw(1)
    assert str(j) == "🍪"


def test_deposit():
    j = Jar()
    j.deposit(5)
    assert j.size == 5

    with pytest.raises(ValueError):
        j.deposit(20)


def test_withdraw():
    j = Jar()
    j.deposit(5)
    j.withdraw(2)
    assert j.size == 3

    with pytest.raises(ValueError):
        j.withdraw(10)


def test_getters():
    j = Jar(10)
    assert j.size == 0
    assert j.capacity == 10
