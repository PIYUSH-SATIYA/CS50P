import validators

def main():
    emailAddress = input("What's your email address? ")
    isValid = validators.email(emailAddress)

    if isValid:
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
