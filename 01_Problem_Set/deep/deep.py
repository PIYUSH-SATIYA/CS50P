def main():
    ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

    if ans == "42":
        print("Yes")
    elif ans == "forty-two":
        print("Yes")
    elif ans == "forty two":
        print("Yes")
    else:
        print("No")

main()
