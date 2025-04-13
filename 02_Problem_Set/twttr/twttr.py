str = input("Input: ")

print("Output: ", end="")
for i in str:
    if i in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
        continue
    else:
        print(i, end="", sep="")
print()