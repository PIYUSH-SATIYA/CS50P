def meow(n: int) -> None:
    for _ in meow(n):
        print("meow")

number: int = int(input("Number: "))
meow(number)