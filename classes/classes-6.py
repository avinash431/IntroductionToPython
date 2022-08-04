class Parent:
    def __init__(self):
        print("THis is a parent class")


class Parent2:
    def __init__(self):
        print("This is a parent2 class")


class Child(Parent2, Parent):
    def __init__(self, x, y):
        super(Child, self).__init__()
        self.x = x
        self.y = y


c = Child(2, 3)
print(c.x, c.y)
