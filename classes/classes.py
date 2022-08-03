class Sample:
    x = 10
    y = "abc"
    z = True
    k = 10.93

    def __init__(self):
        print("This is an initializer")

    def method1(self):
        print("This is a method in a class Sample")

    def method2(self):
        print("This is another method in a class")

    def method3(self, a, b):
        return a + b

    def method4(self):
        print(self.x, self.y, self.k, self.z)


s = Sample()
s.method1()
s.method2()
s.method4()
print(s.method3(4, 5))
