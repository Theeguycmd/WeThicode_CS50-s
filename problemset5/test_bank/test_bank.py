from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello, world!") == 0
    assert value("HELLO") == 0


def test_startWhithH():
    assert value("hi, how are you doing") == 20
    assert value("hi") == 20


def test_any():
    assert value("What's happening?") == 100
