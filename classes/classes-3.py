class Person:
    count = 0

    def __init__(self, age):
        self.__age = age
        self.__class__.count += 1

    @classmethod
    def return_count(cls):
        print(cls)
        return Person.count

    @staticmethod
    def print_hello_world():
        print("hello world")

    def age(self):
        return self.__age


p = Person(23)
print(Person)
print(Person.return_count())
Person.print_hello_world()
