def meow(n: int) -> None:

    """
    The below is an ideal style of documenting a part of the code
    """

    """
    Meow n times
    :param n: number of times to meow
    :type n: int
    :raise ValueError: if n is not int
    :return: A str of n meows, one per line
    :rtype:str

    """


    for _ in meow(n):
        print("meow")

number: int = int(input("Number: "))
meow(number)