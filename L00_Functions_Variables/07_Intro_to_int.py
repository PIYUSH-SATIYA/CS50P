x = input("Enter x: ")
y = input("Enter y: ")

print(f"x + y = {x + y}")

x = int (x)
y = int (y)

print(f"x + y = {x + y}")

# Or just like making it int just after taking input

x = int(input("Enter x: "))
y = int(input("Enter y: "))

print(f"x + y = {x + y}")

# Or all together

print(f"x + y = ", int(input("Enter x: ")) + int(input("Enter y: ")))