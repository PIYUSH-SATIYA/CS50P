def main():
    greet = input("Greeting: ").lower().strip()
    value(greet)

def value(greet):
    greet = greet.lower().strip()
    if greet.startswith("hello"):
        return 0
    elif greet.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
