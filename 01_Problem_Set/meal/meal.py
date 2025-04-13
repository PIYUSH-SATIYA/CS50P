def main():
    time = input("What time is it? ").strip()
    t = float(convert(time))

    if 7.0 <= t <= 8.0:
        print("breakfast time")

    elif 12.0 <= t <= 13.0:
        print("lunch time")

    elif 18.0 <= t <= 19.0:
        print("dinner time")

def convert(time):
    first, second = time.split(":")
    first = float(first)
    second = float(second) / 60
    return (first + second)


if __name__ == "__main__":
    main()
