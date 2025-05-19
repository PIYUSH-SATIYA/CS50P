def main():
    word = input("Input: ")
    str = shorten(word)
    print(str)


def shorten(word):
    str = ""
    for i in word:
        if i in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
            continue
        else:
            str += i

    return str


if __name__ == "__main__":
    main()
