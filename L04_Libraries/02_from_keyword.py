# from random import choice
import random

p = random.choice(["Heads", "Tail"])

print(p)

q = random.randint(1, 10)

print(q)

k = ["piyush", "satiya", "money", "rich"]


print(k)

random.shuffle(k)
# unlike other functions it doesn't returns anything, it just changes the original list itself

print(k)