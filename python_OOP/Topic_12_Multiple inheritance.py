# Create two parent classes Animal and Bird, each with a method that prints a message.
# Then create a child class Parrot that inherits from both and calls both methods.

class Animal:
    def eat(self):
        print("Animal can eat.")

class Bird:
    def fly(self):
        print("Bird can fly.")

class Parrot(Animal, Bird):
    pass

p = Parrot()
p.eat()
p.fly()


# Create two parent classes with attributes, then create a child class that inherits both and prints both attributes using multiple inheritance.

class Father:
    def __init__(self):
        self.father_name = "John"

class Mother:
    def __init__(self):
        self.mother_name = "Emma"

class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
        print("Father's Name:", self.father_name)
        print("Mother's Name:", self.mother_name)

c = Child()


# Create two parent classes with the same method name to observe Method Resolution Order (MRO) in multiple inheritance.

class ClassA:
    def show(self):
        print("This is ClassA")

class ClassB:
    def show(self):
        print("This is ClassB")

class ClassC(ClassA, ClassB):
    pass

obj = ClassC()
obj.show()  # MRO will call ClassA's show() first


# Create a Shape class with area method and a CostCalculator class with cost method.
# Create a class LandPlot that inherits both to calculate total cost using area and cost per square unit.

class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class CostCalculator:
    def __init__(self, cost_per_unit):
        self.cost_per_unit = cost_per_unit

    def calculate_cost(self, area):
        return area * self.cost_per_unit

class LandPlot(Shape, CostCalculator):
    def __init__(self, length, width, cost_per_unit):
        Shape.__init__(self, length, width)
        CostCalculator.__init__(self, cost_per_unit)

    def total(self):
        a = self.area()
        cost = self.calculate_cost(a)
        print("Area:", a)
        print("Total Cost:", cost)

plot = LandPlot(30, 20, 15)
plot.total()
