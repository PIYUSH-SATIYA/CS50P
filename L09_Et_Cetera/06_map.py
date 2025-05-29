def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = map(str.upper, words)
    """
        Instead of running a for loop to capitalize and accumulate in a list each of the word of the list words, we can pass it as the iterable with the function upper, which then will be run for each of them by the funcion map().
    """
    print(*uppercased)

if __name__ == "__main__":
    main()