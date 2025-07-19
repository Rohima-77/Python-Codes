from math import pi

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)


circle = Circle(5)
print(f"Circle Area: {circle.area():.2f}")
print(f"Circle Perimeter: {circle.perimeter():.2f}")

rectangle = Rectangle(4, 6)
print(f"Rectangle Area: {rectangle.area()}")
print(f"Rectangle Perimeter: {rectangle.perimeter()}")
