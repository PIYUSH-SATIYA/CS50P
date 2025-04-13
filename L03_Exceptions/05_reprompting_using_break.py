# It would be more user friendly if we keep prompting user for the correct type of input insetead of just quitting the programme if the user makes the error once only

while True:
    try:
        x = int(input("Enter x: "))
    except ValueError:
        print("Enter an integer!!!")
    else:
        break   # when everything went fine means the user has entered correct type of input

print()
print(f"x is {x}")