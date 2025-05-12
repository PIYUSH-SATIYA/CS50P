import sys

try:
    print("hello,", sys.argv[1]) # it will take first ever elem from the list of args provided in the CLI (argv) and put it here, space is put by default
except IndexError:
    print("Too few arguments")
    sys.exit("Exiting...")

for arg in sys.argv[:3]:
    print("Hello,", arg)


print("End Successfully")

# we indexed the first argument additionally typed as argv[1] and not argv[0] becasue the very first argument is the name of the programe itself adn any arguments passed in addition to it is first, second etc.

# in teminal type python3 04_name.py any_argument(here_name)

# it throws IndexError when no argument is passed

