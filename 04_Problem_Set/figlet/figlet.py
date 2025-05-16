import pyfiglet
import sys

str = input("Input: ")

if len(sys.argv) == 1:
    print(pyfiglet.figlet_format(str))
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "-font"):
    print(pyfiglet.figlet_format(str, font=sys.argv[2]))
else:
    sys.exit("Invalid usage")