from datetime import datetime, date
import re, sys, inflect


def main():
    print("Date format: YYYY-MM-DD")
    print(sayIt(input("Enter a date of birth: ")))


def sayIt(datebirth):
    say = inflect.engine()
    try:
        year, month, day = re.search(r"(\d{4})-(\d{2})-(\d{2})", datebirth).groups()
        valid_month = date(int(year), int(month), int(day))
    except (AttributeError, ValueError):
        sys.exit("Invalid date")
    else:
        something = say.number_to_words(dayMinute(yearDays(valid_month)))
        return f"{something} minutes"


def yearDays(birthDay):
    Date = datetime.now().date()
    diff = Date - birthDay
    return diff.days

def dayMinute(day):
    #todaysHours = datetime.now().time()
    toAdd = day * 24 * 60
    return toAdd #+ (todaysHours.hour * 60) + todaysHours.minute


if __name__ == "__main__":
    main()
