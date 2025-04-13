def coke():
    amount = 0
    while True:
        coin = int(input("Insert Coin: "))

        if coin == 5:
            amount += coin

        elif coin == 10:
            amount += coin

        elif coin == 25:
            amount += coin

        if amount < 50:
            print("Amount Due:", 50 - amount)

        if amount >= 50:
            print("Change owed: ", int(amount - 50))
            break

coke()