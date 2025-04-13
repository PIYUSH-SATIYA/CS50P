try:
    x = int(input("Enter x: "))
except ValueError:
    print("Enter integer only!!!")
else:
    print(f"x is : {x}")