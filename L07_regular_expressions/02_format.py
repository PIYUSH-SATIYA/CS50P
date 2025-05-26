import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), ?(.+)$", name):
# here in the name string we are expecting the user's name in string name, in the format like any set of characters one or time then a comma with optionally space and then some more characters. 
# We have made two groups of characters before and after the comma and storing in matches.
    print(f"hello {matches.group(1)} {matches.group(2)}")
print(name)

#The short way to write the below lines is written as above

# if matches:
#     print(f"hello {matches.group(1)} {matches.group(2)}")
# else:
#     print(name)
