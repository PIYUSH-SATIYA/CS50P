import sys, csv, tabulate

count = 0
if(len(sys.argv)) == 2:
    if not (sys.argv[1].endswith(".csv")):
        sys.exit("Not a CSV file")
    try:
        with open(sys.argv[2], "r") as menu:
            menuTable = csv.DictReader(menu)
            print(tabulate(menuTable, headers=["Sicilian Pizza", "Small", "Large"], tablefmt="grid"))
    except FileNotFoundError:
            sys.exit("File does not exists")


elif(len(sys.argv) < 2):
    sys.exit("Too few command-line arguments")
elif(len(sys.argv) > 2):
    sys.exit("Too many command-line arguments")

print(count)