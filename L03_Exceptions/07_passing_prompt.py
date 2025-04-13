def main():
    x = get_int("Enter X: ")    # We have passed the whole prompt to the functino instead of hardcoring it in that function we made the get_int function more reusable

    print(f"x is {x}")

def get_int(prompt):    # We can call anything instead of prompt, it is just like any other argument
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()