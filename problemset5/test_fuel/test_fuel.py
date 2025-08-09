from fuel import convert, gauge

def test_exceptions():
    assert convert("4/0") == "Error"
    assert convert("three/four") == "Error"
    assert convert("1.5/3") == "Error"
    assert convert("-3/4") == "Error"

def test_improperF():
    assert convert("5/4") == "Error"

def test_full():
    assert gauge(100) == "F"
    assert gauge(99) == "F"


def test_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_percent():
    assert gauge(75) == "75%"
