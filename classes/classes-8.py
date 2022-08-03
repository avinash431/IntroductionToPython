class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def __len__(self):
        return 2

    def __repr__(self):
        return f"x-coordinate is {self.x} and y-coordinate is {self.y}"
    

p1 = Point(2, 3)
p2 = Point(4, 5)
print(p1 + p2)
print(len(p1))
print(p1)
