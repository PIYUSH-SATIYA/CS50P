import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM) to ([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM)$"
    match = re.match(pattern, s)
    if not match:
        raise ValueError("Invalid time format")

    sh, sm, sp, eh, em, ep = match.groups()

    sm = int(sm) if sm else 0
    em = int(em) if em else 0

    sh = int(sh)
    eh = int(eh)

    if sp == "PM" and sh != 12:
        sh += 12
    elif sp == "AM" and sh == 12:
        sh = 0

    if ep == "PM" and eh != 12:
        eh += 12
    elif ep == "AM" and eh == 12:
        eh = 0

    return f"{sh:02}:{sm:02} to {eh:02}:{em:02}"

if __name__ == "__main__":
    main()
