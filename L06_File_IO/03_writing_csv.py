import csv

name = input("Name: ")
house = input("House: ")

# with open("L06_File_IO/name.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, house])


with open("L06_File_IO/name.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "House"])
    writer.writerow({"Name": name, "House": house})