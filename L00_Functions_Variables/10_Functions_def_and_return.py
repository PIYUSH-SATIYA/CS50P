"""
Conventionally we write a main part and write the main function to keep things organized
Also call it 
"""

def main():
    x = int(input("Enter x: "))
    print("The x squared is:", square(x))

def square(n):
    return n * n

main()