# Create class Vehicle with method move().
# Override move() in Car and Boat.
# Loop through list of objects and call move().
class Vehicle :
    def move(self):
        print("vehicle moving")
class Car(Vehicle):
    def move(self):
        print("Car moving")
class Boat(Vehicle):
    def move(self):
        print("Boat moving")

vehicles = [Car(), Boat()]

for v in vehicles:
    v.move()

# Create class Circle and Square with method draw().
# Write a function show_shape(shape) that calls draw().
class circle:
    def draw(self):
        print("drawing circle")

class square:
    def draw(self):
        print("square drawing")

def show_shape(shape):
    shape.draw()
show_shape(circle())
show_shape(square())


# Create two classes: Pen and Pencil. Each should have a method write().
# Create a function start_writing(tool) that calls write() using polymorphism.
# Pass both Pen and Pencil objects to the function.
class Pen:
    def write(self):
        print("Writing with a pen")

class Pencil:
    def write(self):
        print("Writing with a pencil")

def start_writing(tool):
    tool.write()

start_writing(Pen())
start_writing(Pencil())


