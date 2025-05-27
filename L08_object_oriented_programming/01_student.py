class Student:
    def __init__(self, name, house):
        # we can here check for condition also before taking input and raise errors as and when necessary
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name:")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()