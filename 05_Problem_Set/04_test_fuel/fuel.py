def main():
    while True:
        str = input("Input: ")
        convert(str)



def convert(fraction):
    try:
        x, y = fraction.split('/')
        gauge(round(int(x)/int(y)))
        return (round(int(x)/int(y)))
    except (ValueError, ZeroDivisionError):
            pass

def gauge(percentage):
    if percentage <= 0.01:
            return "E"
    elif percentage >= 0.99 and percentage <= 1.00:
            return "F"
    elif 0.01 < percentage < 0.99:
            return (f"{round(percentage*100)}%")


if __name__ == "__main__":
    main()
