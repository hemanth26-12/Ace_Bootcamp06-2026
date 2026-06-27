from abc import ABC
import math
class Shape:

    def __init__(self,r,b,h):
        self.r = r
        self.b = b
        self.h = h
    def area(self):
        pass
    def perimeter(self):
        pass
class Circle(Shape):
      def __init__(self,r):
        self.r = r
      def area(self):
        return math.pi*(self.r**2) 
      def perimeter(self):
        return math.pi*self.r*2
    
class Triangle(Shape):
    def __init__(self, r, b, h):
        super().__init__(r, b, h)   

    def area(self):
        return 0.5*self.b*self.h 
    def perimeter(self):
        return self.r + self.b +self.h
    
class Square(Shape):
    def __init__(self, r, b, h):
        super().__init__(r, b, h)

    def area(self):
        return self.r**2
    def perimeter(self):
        return 4*self.r 
s1 = Shape(4,5,5)    
c1 = Square()
t1 = Triangle()
s1 = Circle()


print(c1.area())
print(c1.perimeter())
print(t1.area())
print(t1.perimeter())
print(s1.area(4))
print(s1.perimeter())


    
