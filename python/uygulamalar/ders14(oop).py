#OOP 1
class Vehicle:
    def __init__(self,brand,model,color):
        self.brand=brand
        self.model=model
        self.color=color

car1_obj=Vehicle("Skoda","Superb","White")
car2_obj=Vehicle("Honda","Civic","Green")

print(car1_obj.brand,"-",car1_obj.model,"-",car1_obj.color)
print(car2_obj.brand,"-",car2_obj.model,"-",car2_obj.color)

print("\n")



#OOP 2

class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def __str__(self):
         return f"Name:{self.name}\nAge:{self.age}"
    def __repr__(self):
        return f"Name:{self.name!r}\nAge:{self.age!r}"
    
    def myInfo(self):
        print(f"Hello my name is {self.name}")
        print(f"I am {self.age} years old")
p1=Person("Emir",19)
print(p1)
print(repr(p1),"\n")
p1.myInfo()