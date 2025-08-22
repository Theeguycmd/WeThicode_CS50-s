from numb3rs import validate


def test_words():
    assert validate("Cat") == False
    assert validate("cat") == False
    assert validate("CAT") == False

def test_bigger():
    assert validate("123.345.2.4") == False

def test_negative():
    assert validate("-123.276.-2.-90") == False

def test_right():
    assert validate("2.234.70.21") == True 
