def total(num1, num2, num3):
    return num1 + num2 + num3

numbers = [10, 15, 20]

print(f"{total(*numbers)} is the total")
# print(total(num1=10, num3=20, num2=15))