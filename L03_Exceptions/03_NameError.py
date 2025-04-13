# We get name error when the variable/function/object we tried to use has not been defined or is not acccesddible in the currnt scope

try:
    x = int(input("Enter x: "))
except ValueError:
    print("Enter an integer !!!")

print("x is: ", x)

# When a non integer value is entered the int function cant assign a value to x, hence x is undefined.
# Therefore printing x in such case will show an NameError