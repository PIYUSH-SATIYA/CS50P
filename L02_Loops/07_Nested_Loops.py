def main():
    print_Square(5)

def print_Square(size):
    for i in range(size):

        for j in range(size):

            print("#", end= "")

        print()

"""

This can also be done
def print_Square(size):
    print("#" * size)

"""

main()