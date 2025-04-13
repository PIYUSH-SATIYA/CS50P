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
    try:
        x = input("Date: ")
        if '/' in x:
            month, day, year = x.split('/')
            month = int(month)
            day = int(day)
            year = int(year)
            if 0 < day < 32 and (0 < month < 13) and day not in months:
                print(f"{year:0004}-{(month):02}-{day:02}")
                break
        else:
            month, day, year = x.split(' ')
            month = month.strip().removesuffix(',').capitalize()
            month = months.index(month)

            if ',' in day:
                day = day.removesuffix(',')
                day = int(day)
                year = int(year)

            if 0 < day < 32 and (0 < month < 13) and day not in months:
                print(f"{year:0004}-{(month + 1):02}-{day:02}")
                break
            else:
                pass

    except (ValueError, TypeError):
        pass




