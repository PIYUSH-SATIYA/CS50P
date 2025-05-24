import sys

count = 0
if(len(sys.argv)) == 2:
    if not (sys.argv[1].endswith(".py")):
        sys.exit("Not a python file")
    try:
        with open(f"{sys.argv[1]}", "r") as file:
            listOfLines = file.readlines()
            for line in list:
                if(line.strip() != "" and line.strip()[0] != "#"):
                    count += 1
    except FileNotFoundError:
            sys.exit("File does not exists")
            

elif(len(sys.argv) < 2):
    sys.exit("Too few command-line arguments")
elif(len(sys.argv) > 2):
    sys.exit("Too many command-line arguments")

print(count)