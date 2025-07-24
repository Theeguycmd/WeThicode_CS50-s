import sys

def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    while True:
        date = input("Date: ")
        if "/" in date:
            mm, dd, yyyy = date.split("/")
            if len(yyyy) == 4:
                sys.exit(f"{int(yyyy)}-{int(mm):02d}-{int(dd):02d}")
        elif date.split()[0].title() in months and "," in date.split()[1]:
            m, d, yy = date.split()
            d = int(d.replace(",", ""))
            m = m.title()
            sys.exit(f"{yy}-{months.index(m) + 1:02d}-{d:02d}")
        else:
            pass


if __name__ == "__main__":
    main()
