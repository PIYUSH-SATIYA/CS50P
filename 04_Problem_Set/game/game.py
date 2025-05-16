import random


while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        continue


p = random.randint(1, n)

while True:
    try:
        user = int(input("Guess: "))
        if user < p:
            print("Too small!")
        elif user > p:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        continue
