import re

email = input("what's your email address: ").strip()

# if re.search("^.+@.+\\.com$", email):   # This means that any char apearing once or more (due to +) then an @ symbol then also any char appearing once or more and ^ and $ just marks start and the end of the string means, whlole expression must be like this only and without it if only a part mathces than also it would have marked it true.
#     # the \\. means a literal '.' which means at the end there should be .com and not anything 
#     print("Valid")
# else: 
#     print("Invalid")


# we could have written more like this also

# Another approach

# if re.search("^.+[^@]+@[^@]+\\.com$", email): # this means that only one @ sign are allowed, all char are allowed before and after the char but the @ (one or more occurences).  
#     print("valid")

# else:
#     print("Invalid")

# Another approach


# stands for raw string which is necessary for using some escape sequence characters using `\` zxz
if re.search(r"^\w+@\w+\.(com|ac.in|org)$", email, re.IGNORECASE): # this means that only one @ sign are allowed, all char are allowed before and after the char but the @ (one or more occurences).  
    print("valid") 

else:
    print("Invalid")