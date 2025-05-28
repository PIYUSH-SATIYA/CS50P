import argparse as agp

parser = agp.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n",default=1, help="number of time to meow")
args = parser.parse_args()

"""
    using the argparser we parse a cli argument n which is handled like this :

    if len(sys.argv) == 3 and sys.argv[1] == "-n":
        args.n = sys.argv[2]

        the description and help tags are shown when a user passess --help switch

        When no args are passed, the default one is passed, here 1
"""


def meow(n: int) -> None:
    for _ in range(n):
        print("meow")

# number: int = int(input("Number: "))
# meow(number)


meow(int(args.n))