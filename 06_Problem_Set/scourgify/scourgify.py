import sys, csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")


try:
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

with open(sys.argv[2], "w", newline="") as newFile:
    writer = csv.DictWriter(newFile, fieldnames=["first", "last", "house"])
    writer.writeheader()
    count = 0

    for line in lines[1:]:
        namePart, house = line.strip().split('",')
        namePart = namePart.replace('"', '')
        last, first = namePart.split(', ')
        house = house.strip()
        writer.writerow({"first": first, "last": last, "house": house})
