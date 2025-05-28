class Student:
    def __init__(self, name, house):
        # we can here check for condition also before taking input and raise errors as and when necessary
        self.name = name
        self.house = house
        # these names of the variables after self may be anything, but wahtever it be those names will be used to access the attributes of an object.
        # the actual name and house passed to the dunder init method are just plain variables nothing more.


    # def greet(self):
    #     return f"{self.name} saying you hello"


    # # A class method(2nd file) to initiate a student, from the class itself just for good code design.  
    # @classmethod
    # def get(cls):
    #     name = input("Name: ")
    #     house = input("House: ")
    #     return cls(name, house) # returns a object by calling the class itself, i.e. running the __init__ method of the class internally.

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name!!!")
        else:
            self._name = name

    @property
    def house(self):
        # print("Getter accessed")
        return self._house
    @house.setter
    def house(self, house):
        # print("setter accessed")
        if house in ["Gryffindor", "Hufflepuf", "Ravenclaw", "Slytherine"]: # Just like this we can define some validating condition before setting the value of the attribute. 
            self._house = house
        else:
            raise ValueError("Invalid Name!!!")




def main():
    # student = Student.get("harry", "gryffindor")
    # by this line we can create an obect if we want to use the above classmethod
    student = get_student()
    print(f"{student.name} from {student.house}")
    # print(student.greet())


def get_student():
    name = input("Name:")
    house = input("House: ")
    return Student(name, house)

# we can clean up function because the only thing it is doing is helping to make an object, which ideally shoudl be the functionality of the class to serve it's purpose nicely.  


if __name__ == "__main__":
    main()