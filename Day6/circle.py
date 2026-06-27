import math
class Circle:
    def __init__(self,rad):
        self.rad = rad
    def area(self):
        return math.pi*(self.rad**2)
    def perimeter(self):
        return math.pi * 2 * (self.rad)

c1 = Circle(20)
print(c1.area())
print(c1.perimeter())