# with open("L06_File_IO/name.csv") as file:
#     for line in file:
#         row = line.strip().split(",")
#         print(f"{row[0]}, {row[1]}, {row[2]}, {row[3]}")

# now the above code will not be able to read the csv file properly because the name in the 5th row has a commadn itself in the name so we have to use the csv library

import csv

# with open("L06_File_IO/name.csv") as file:
#     reader = csv.reader(file)
#     for row in reader:
        # print(f"{name}, {age}, {car1}, {car2}")

# we kept it like the name in the last row to be having comma in its name itself and not the separator comma, so we enclosed it in the quotes and csv module handled it

# Reading Dictionary

with open("L06_File_IO/name.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"'Name': {row['Name']}, 'House': {row['House']} ")
        