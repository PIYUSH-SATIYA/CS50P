def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("x is even")
    else:
        print("x is odd")

def is_even(n):
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False

    # whole of the above if else can be collapsed like this, like a simple english
    return True if n % 2 == 0 else False

    """
        The most readable and and elegant way is
        return n % 2 == 0    
            it means is n % 2 == 0 is true than true is returned otherwise false is returned
    """

main()