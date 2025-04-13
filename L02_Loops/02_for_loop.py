# There are two ways of initialising the for loop

# Here i will take values of each elements from the list
for i in [0, 2, 4, "hi"]:
    print("hello ", i)

# Here j will take values from 0 to 4
for j in range(5):
    print(j, " Hello")

# To use a variable just to count something it is not gonna be used further we name it as _ conventionally to let ourself and other ones know it is just for counting

for _ in range(7):
    print("Convention")

print("Woof\n" * 5, end = "")   # concatenated woof\n 5 times ot itself and as \n is already in last we set end=""