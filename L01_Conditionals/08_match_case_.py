name = input("What's your name: ").title()

# match name:
#     case "Harry":
#         print("Gryffindor")
#     case "Ron":
#         print("Gryffindor")
#     case "Hermione":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:                 #This is the default case
#         print("Who? ")

match name:
    case "Harry" | "Ron" | "Hermione" :     # This is or operation 
        print("Gryffindor")
    case "Draco":
        print("Sletheryine")
    case _:
        print("Who?")