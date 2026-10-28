from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        ...

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return 2*(self.height+self.width)
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return 3.1415*self.radius**2
    def perimeter(self):
        return 2*3.1415*self.radius

circle=Circle(3)
print("Area:",circle.area())
print("Perimeter:",circle.perimeter())

rect=Rectangle(4,7)
print("Area:",rect.area())
print("Perimeter:",rect.perimeter())
