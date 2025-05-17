from square import sq

# def main():
#     test_sq()

# def test_sq():
#     # if sq(2) != 4:
#     #     print("2 squared was not 4")
#     # if sq(3) != 9:
#     #     print("3 sqaured was not 9")

#     assert sq(2) == 4
#     try:
#         assert sq(3) == 9
#     except:
#         print("3 aquared was not 9")
#     # this throws assertionError if the assertion is false
#     # we can print some error message with try and except keywords like try to assert exvept the assertion error and prin the error message

# if __name__ == "__main__":
#     main()

# for pytest


def test_sq():
    assert sq(5) == 4
    assert sq(1) == 1
    assert sq(5) == 25
    assert sq(6) == 36
    assert sq(4) == 16