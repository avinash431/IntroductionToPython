class Person:
    def method1(self):
        print("This is a method1 in person class")

    def method2(self):
        print("This is a method2 in person class")


class Child(Person):
    def method1(self):
        print("This is is method1 in child class")


c = Child()
c.method1()
c.method2()
