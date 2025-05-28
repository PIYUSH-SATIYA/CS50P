import datetime as d
import sys
import re
import inflect

p = inflect.engine()


dob = input("Date of Birth: ")
# year_td, month_td, day_td = int(d.date.today().split("-"))

if re.search(r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$", dob):
    # year, month, date = match.split("-")
    dob = d.datetime.strptime(dob, "%Y-%M-%d")

    gap = d.datetime.strptime((d.date.today().strftime("%Y-%M-%d")), "%Y-%M-%d") - dob
    print(f"{p.number_to_words(int(gap.total_seconds()/60))}")
else:
    sys.exit("Invalid date")

    