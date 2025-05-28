class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name!!!")
        else:
            self.name = name

class Student(Wizard):
    def __init__(self,name,  house):
        self.house = house
        super().__init__(name)  # This is a way of telling that for name use the init method of the parent class.


class Professor(Wizard):
    def __init__(self,name, subject):
        self.subject = subject
        super().__init__(name)

wizard = Wizard("Albus Dumbledore")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense against the dark arts")