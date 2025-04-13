camel = input("camelCase: ").strip()

for i in camel:
    if 65 <= ord(i) <= 90:
        print("_", i.lower(), sep="", end="")
    else:
        print(i, sep="", end="")
print()