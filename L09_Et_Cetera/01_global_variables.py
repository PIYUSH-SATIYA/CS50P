balance = 0

def main():
    print("Balance: ", balance)
    deposite(100)
    withdraw(10)
    print("Balance: ", balance)

def deposite(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n


if __name__ == "__main__":
    main()