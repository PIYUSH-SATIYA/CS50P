#single line comment
name = input("What's your name? ")
print("Hello name")

"""
this is a multiline comment
"""

# print("hello")
# print(name)

#a better way
print("Hello, " + name + name) #this whole is only one argument formed by concatenation of three arguments by + operator
print("hello,", name, name) #There are 3 args now passed individually separated by a , python automatically separates them by adding a space in outputs