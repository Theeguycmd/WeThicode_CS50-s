from seasons import sayIt
from datetime import date


todayDate = date.today()
yearAgo = date(todayDate.year - 1, todayDate.month, todayDate.day)
year2Ago = date(todayDate.year - 2, todayDate.month, todayDate.day)


def test_sayIt():
    global yearAgo, year2Ago
    assert sayIt(str(yearAgo)) == "five hundred and twenty-five thousand, six hundred minutes"
    assert sayIt(str(year2Ago)) == "one million, fifty-two thousand, six hundred and forty minutes"
