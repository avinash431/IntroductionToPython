class Humans:
    x = 1

    def __init__(self):
        print("this is init method")
        self.y = None

    def sample(self):
        self.y = 12
        print("this is method1")

    def sample2(self):
        print("this is sample2")


h1 = Humans()

