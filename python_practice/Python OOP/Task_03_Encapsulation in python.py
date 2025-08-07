"""Your task is to create a Person class in Python that demonstrates encapsulation. This class should have two "private" attributes:

name (String) with a default value of "Geeks".
age (int) with a default value of 10.
The class should provide public methods to access and modify these private attributes:

Getter Methods: get_name() and get_age()
Setter Methods: set_name(name) and set_age(age)"""
class Person:
    def __init__(self):
        self.__name = "Geeks"
        self.__age = 10
    def get_name(self):
        print(self.__name)
    def get_age(self):
        print(self.__age)
    def set_name(self,name):
        self.__name = name
    def set_age(self,age):
        self.__age = age
obj = Person()

obj.get_name()
obj.get_age()

obj.set_age(19)
obj.set_name("john")

obj.get_name()
obj.get_age()