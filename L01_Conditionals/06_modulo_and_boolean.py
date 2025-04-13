def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("x is even")
    else:
        print("x is odd")

# The is_even(n) function is a boolean function
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# The modulo operator returns the remainder when the left operand is divided by the right operand

main()