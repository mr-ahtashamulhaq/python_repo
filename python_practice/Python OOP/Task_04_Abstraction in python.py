"""Class Name: Shape (Abstract Class)
Attributes: color (String)
Constructor: Shape(c) -> assign value of c to color attribute
Methods: get_color() -> returns value of color
         get_area() -> abstract method with float return type
         
Class Name: Square (extends Shape)
Attributes: side (float)
Constructor: Square(c, side) -> calls super(c) to initialize the color and assigns the value to side.
Methods: get_area() -> returns the area of the square (side * side)."""
from abc import ABC,abstractmethod

class Shape(ABC):
    def __init__(self,c):
        self.color = c
    def get_color(self):
        return self.color
    @abstractmethod
    def get_area(self) -> float:
        pass
    
class Square(Shape):
    def __init__(self,c,side):
        super().__init__(c)
        self.side  = side
    def get_area(self):
        return self.side*self.side

obj = Square("red", 5.0)
print(obj.get_color())
print(obj.get_area())