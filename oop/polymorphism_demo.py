import math

class Shape:
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width 

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

if __name__=="__main__":
    shapes = [
        Rectangles(4, 5),
        Circle(3)
    ]

    for shape in shapes:
        print(f"{shape.__class__.__name__} Area: {shape.area():.2f}")