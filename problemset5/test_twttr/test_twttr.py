from twttr import shorten

def test_lowerCase():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_noVowels():
    assert shorten("CS50") == "CS50"

def test_combination():
    assert shorten("Hello, WORLD!") == "Hll, WRLD!"

def test_upperCase():
    assert shorten("HELLO, WORLD") == "HLL, WRLD"
