import random

def main():
    score = 0

    level = get_level()

    for _ in range(10):
        num = generate_integer(level)
        a = random.choice(num)
        b = random.choice(num)

        for i in range(3):
            try:
                ans = int(input(f"{a} + {b} = "))
                if ans == a + b:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")

        if i == 2 and ans != a + b:
            print(f"{a + b}")

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            lvl = int(input("level: "))
            if lvl in [1, 2, 3]:
                return lvl
        except ValueError:
            pass

def generate_integer(level):
    numbers = []
    for _ in range(10):
        a, b = generate_integer(level)
        numbers.extend([a, b])
    return numbers

if __name__ == "__main__":
    main()
