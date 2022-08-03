class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return self.x + self.y

    def __del__(self):
        print("This is a destructor")


p = Point(2, 3)
print(p.x, p.y)
print(p.distance())
