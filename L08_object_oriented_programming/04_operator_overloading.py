class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


v1 = Vector(input("x1: "), input("y1: "))
v2 = Vector(input("x2: "), input("y2: "))
v3 = v1 + v2

print(v3)
