while True:

    try:
        x, y = input("Fraction: ").split('/')
        ans = int(x)/int(y)

    except (ValueError, ZeroDivisionError):
        pass
    else:
        if ans <= 0.01:
            print("E")
            break
        elif ans >= 0.99 and ans <= 1.00:
            print("F")
            break
        elif 0.01 < ans < 0.99:
            print(f"{round(ans*100)}%")
            break
