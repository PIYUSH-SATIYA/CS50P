grocery = {}

while True:
    try:
        item = input().upper()
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1


    except EOFError:
        grocery = dict(sorted(grocery.items()))
        for key, value in grocery.items():
            try:
                print(f"{value} {key}")
            except KeyError:
                pass
        break
    except KeyboardInterrupt:
        print()
        break

