from um import count

def test_upper():
    assert count("UM") == 1
    assert count("UM, GOOD DAY UM, EVERYONE UM, THIS IS YUMMY") == 3

def test_lower():
    assert count("um") == 1
    assert count("um,") == 1
    assert count("um, good day um, everyone um, this is yummy") == 3

def test_other():
    assert count("hello everyone") == 0
    assert count("Um") == 1
