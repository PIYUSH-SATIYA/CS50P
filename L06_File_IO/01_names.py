file = open("./L06_File_IO/names.txt", "a")

for _ in range(3):
    # file.write(f"{input("Enter Name: ")}\n")

    # file.close() 

    with open("./L06_File_IO/names.txt", "a") as file:
        file.write(f"{input("Enter Name: ")}\n")

    
with open ("./L06_File_IO/names.txt", "r") as f: # it could be sorted(f) to sort the file in ascending order
    for l in f:
        print(f"this is: ", l.rstrip())