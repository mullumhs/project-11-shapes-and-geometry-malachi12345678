import math

class Shape:
    def area(self):
        pass

    def perimeter (self):
        pass

class Rect(Shape):
    def __init__(self , width , height):
        self.height = height
        self.width = width

    def area(self):
        return self.width * self.height 

    def perimeter (self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self , radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter (self):
        return 2 * math.pi * self.radius

