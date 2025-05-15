def main():
    hello("world")
    bye("world")

def hello(name):
    print(f"hello {name}")

def bye(name):
    print(f"goodbye, {name}")

if __name__ == "__main__":
    main()

    # When this file is run by CLI the special symbol '__name__' is set to be __main__ , that's why we said to call the main function only if this program is run by CLI 
    # howeever if this file is imported as a module in some other file, only some function of the file are required to be, and if this is imported as a module than the value of the symbol __name__ is set to be the name it is imported as. So the main function is not executed as we wanted.