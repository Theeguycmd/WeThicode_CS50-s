import pytest
from jar import Jar


def test_init():
    jar = Jar(5)
    assert jar.size == 0
    assert jar.capacity == 5


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12 
    jar.deposit(3)
    assert jar.size == 3
    assert jar.capacity == 9

def test_withdraw():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12
    jar.deposit(12)
    jar.withdraw(2)
    assert jar.size == 10
    assert jar.capacity == 2


def test_errors():
    jar = Jar(1)
    with pytest.raises(ValueError):
        jar.deposit(2)
        jar.withdraw(2)
