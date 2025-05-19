def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    slice1 = s[0:2]

    if len(s) < 2 or len(s) > 6:
        return False

    for i in s:
        if 0 <= ord(i) < 48 or 57 < ord(i) < 65 or ord(i) > 90:
            return False

    for i in slice1:
        if 47 < ord(i) < 58:
            return False

    count = 0

    for i in s :
        if 47 < ord(i) < 58:
            slice2 = s[count:6]
            break
        count += 1
        slice2 = None

    if slice2 != None:
        for i in slice2:
            if slice2[0] == '0':
                return False
            elif 64 < ord(i) < 91:
                return False

    return True


if __name__ == "__main__":
    main()
