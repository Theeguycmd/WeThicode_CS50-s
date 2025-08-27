import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        num1, num1str, ap1, num2, numstr2, ap2 = re.search(r"(\d{1,2})(:\d{2})? (AM|PM) to (\d{1,2})(:\d{2})? (AM|PM)", s).groups()
    except AttributeError:
        raise ValueError("No matches found")
    
    if ap1 == "PM" and  ap2 == "PM":
        if num1str != None and numstr2 != None:
            return f"{validate_hours(num1)}{validate_minutes(num1str)} to {validate_hours(num2)}{validate_minutes(numstr2)}"
        elif num1str != None and numstr2 == None:
            return f"{validate_hours(num1)}{validate_minutes(num1str)} to {validate_hours(num2)}:00"
        elif num1str == None and numstr2 != None:
            return f"{validate_hours(num1)}:00 to {validate_hours(num2)}{validate_minutes(numstr2)}"
        else:
            return f"{validate_hours(num1)}:00 to {validate_hours(num2)}:00"
    elif ap1 == "PM" and ap2 == "AM":
        if num1str != None and numstr2 != None:
            return f"{validate_hours(num1)}{validate_minutes(num1str)} to {validate_hour(num2)}{validate_minutes(numstr2)}"
        elif num1str != None and numstr2 == None:
            return f"{validate_hours(num1)}{validate_minutes(num1str)} to {validate_hour(num2)}:00"
        elif num1str == None and numstr2 != None:
            return f"{validate_hours(num1)}:00 to {validate_hour(num2)}{validate_minutes(numstr2)}"
        else:
            return f"{validate_hours(num1)}:00 to {validate_hour(num2)}:00"
    elif ap1 == "AM" and ap2 == "PM":
        if num1str != None and numstr2 != None:
            return f"{validate_hour(num1)}{validate_minutes(num1str)} to {validate_hours(num2)}{validate_minutes(numstr2)}"
        elif num1str != None and numstr2 == None:
            return f"{validate_hour(num1)}{validate_minutes(num1str)} to {validate_hours(num2)}:00"
        elif num1str == None and numstr2 != None:
            return f"{validate_hour(num1)}:00 to {validate_hours(num2)}{validate_minutes(numstr2)}"
        else:
            return f"{validate_hour(num1)}:00 to {validate_hours(num2)}:00"
    else:
        if num1str != None and numstr2 != None:
            return f"{validate_hour(num1)}{validate_minutes(num1str)} to {validate_hour(num2)}{validate_minutes(numstr2)}"
        elif num1str != None and numstr2 == None:
            return f"{validate_hour(num1)}{validate_minutes(num1str)} to {validate_hour(num2)}:00"
        elif num1str == None and numstr2 != None:
            return f"{validate_hour(num1)}:00 to {validate_hour(num2)}{validate_minutes(numstr2)}"
        else:
            return f"{validate_hour(num1)}:00 to {validate_minutes(num2)}:00"


def validate_hours(first):
    hour = int(first)
    if 1 <= int(first) <= 12:
        if int(first) == 12:
            return "00"
        else:
            return f"{hour + 12}"
    else:
        raise ValueError("Invalid hours")



def validate_hour(hour):
    n = int(hour)
    if 1 <= n <= 12:
        if n < 10:
            return f"0{n}"
        return n
    else:
       raise ValueError("Invalid hours")




def validate_minutes(first):
    if 0 <= int(first[1:]) <= 59:
        return first
    else:
        raise ValueError("Invalid minutes")




if __name__ == "__main__":
    main()
