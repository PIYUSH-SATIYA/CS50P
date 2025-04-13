students = [
    {"name" : "Hermione", "house" : "Gryffindor", "patronous" : "Otter"},
    {"name" : "Harry", "house" : "Gryffindor", "patronous" : "Stag"},
    {"name" : "Ron", "house" : "Gryffindor", "patronous" : "Jack Russel terrier"},
    {"name" : "Draco", "house" : "Slytherine", "patronous" : None}  # None explicitely declares that the key has no value 
]

for student in students:
    print(student["name"], student["house"], student["patronous"])
    # This list the value associated with keys name, house and patronous for each student in students