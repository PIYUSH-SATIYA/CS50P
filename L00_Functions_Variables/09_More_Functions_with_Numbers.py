x = float(input("Enter x:" ))
y = float(input("Enter y:" ))

z = x + y

print("x + y =", z)
"""
To round off a number

round(number, ndigits=None)

"""
z = round(z, 1)

print("x + y =", z)

"""
Format Specification

:, is thousand separator

:._f is to format a floating point to given no. of digits after decimal

"""

p = x / y

print(f"p = {p:.2f}")

p = round(p)

print(f"{p:,}")

# Note: always use a formatted string to use this