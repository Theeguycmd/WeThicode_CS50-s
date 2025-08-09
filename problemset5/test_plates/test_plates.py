from plates import is_valid


def test_first():
    assert is_valid("CS50") == True

def test_second():
    assert is_valid("CS05") == False

def test_third():
    assert is_valid("CS50P") == False

def test_fourth():
    assert is_valid("PI3.14") == False

def test_fifth():
    assert is_valid("H") == False

def test_sixth():
    assert is_valid("OUTATIME") == False

def test_seventh():
    assert is_valid("HELLO") == True

def test_eight():
   assert is_valid("50") == False 
