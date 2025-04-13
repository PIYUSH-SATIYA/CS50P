first, second, third = input("Expression: ").split(" ")

first = float(first)
third = float(third)

if second == "+":
    print(f"{(first + third):.1f}")
elif second == "-":
    print(f"{(first - third):.1f}")
elif second == "*":
    print(f"{(first * third):.1f}")
elif second == "/":
    print(f"inter{(first / third):.1f}")
