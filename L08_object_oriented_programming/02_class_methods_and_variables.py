import random

class Hat:

    # There is no need to be the same house list for all the student objects to be sorted in those four.  
    # Also there is no need for a separate sorting hat which is the sort method for each object, one would work too.  



    # this houses is a class variable 
    houses = ["Gryffindor", "Hufflepuf", "Ravenclaw", "Slytherine"]

    @classmethod
    def sort(cls, name):    # this has now been passed the cls arg instead.
        print(name, "is in", random.choice(cls.houses)) 
        # as the houses list was a class variable it is accessed by the cls.houses instead of self.houses.


Hat.sort("Harry")