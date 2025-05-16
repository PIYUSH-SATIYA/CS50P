import inflect
p = inflect.engine()

str = input("Input: ")
final = []

while (True):
    try:
        final.append(str)
        str = input("Input: ")
    except EOFError:
        break

print("Adieu, adieu, to " + p.join(final))