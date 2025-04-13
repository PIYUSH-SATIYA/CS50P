name = input("Enter name: ")

print("hello, ", end='')
# As end is a keyword it will not be converted simply into a string
# we just modified the original definition end='\n' to end="" means after the print function ends it will end by "" instead of \n
#"" or '' any of them can be used but fid anyone
print(name)

print("hello, ", name, end='anything ', sep= '&' )
# sep and edn are called named parameters can be used by names only
#what goes first as *object are positional parameters
