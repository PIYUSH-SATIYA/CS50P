name = input("Enter name: ").strip().title()

# # To remove whitespaces from the str
# name = name.strip()

# # To capitalize only the first letter of the string name
# name = name.capitalize()

# print(f"Hello, {name}")
# # To capitalize only the first letter of the string name
# name = name.title()

# print(f"Hello, {name}")

# # To do all the thing at once 
# name = name.strip().title()
# # or do where the input is taken

print(f"Hello, {name}")

# To split the string 
first_name = name.split(" ")
    # This splts the name and returns a sequence of strings after splitting the main strings from wherever the "  " char occurs in their occurence order
    # We can store them in order of the split occured,

print(f"Hello, {first_name}") 

# There are ways in the same functions to split the string some specific number of times and separated by a specific character
