import argparse as agp

parser = agp.ArgumentParser(description="Meow like a cat")  


"""
    This is a constructor for the class ArgumentParse which comes with the library argparse
"""

parser.add_argument("-n",default=1, help="number of time to meow", type=int)  
""" 
    This is the method in the object of class ArgumentParse which allows us to add a command line argument

    :default: this will be passed by defaul when no args are passed
    :type int: specifies the type of argument being passed so that it is not needed to convert thereafter
"""

args = parser.parse_args()  

""" 
    This is the object in which all the cli arguments will be kept parsed, no matter whwatever order in which it are typed, and will be, as allowed and specified by the above methods
    Thet can be accessed like args.argumentNameorSwitch
"""

"""
    using the argparser we parse a cli argument n which is handled like this :

    if len(sys.argv) == 3 and sys.argv[1] == "-n":
        args.n = sys.argv[2]

        the description and help tags are shown when a user passess --help switch

        When no args are passed, the default one is passed, here 1
"""


def meow(n: int) -> None:
    for _ in range(n):
        print("meow")

# number: int = int(input("Number: "))
# meow(number)


meow(args.n)