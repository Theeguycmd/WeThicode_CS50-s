def main():
    time = convert(input("What time is it: "))
    hour, minutes = time.split(":")
    hours = float(hour) + (float(minutes) / 60)

    if hours >= 7 and hours <= 8:
        print("Breakfast time")
    elif hours >= 12 and hours <= 13:
        print("Lunch time")
    elif hours >= 18 and hours <= 19:
        print("Dinner time")
    else:
        print("")


def convert(time):
    time = time.lower()
    if "am" in time or "pm" in time:
        clock, id = time.split()
        if id == "am":
            return clock.strip()
        else:
            hour, minute = clock.split(":")
            hours = int(hour) + 12
            return f"{hours}:{minute}"
    else:
        return time.strip()


if __name__ == "__main__":
    main()
