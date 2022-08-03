class Person:

    def __init__(self):
        self.__name = ""
        self.__age = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise ValueError("Age has to be an integer value")
        if age < 0:
            raise ValueError("Age cannot be -ve")
        self.__age = age
