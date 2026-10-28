class Animal:
    def speak(self):
        return "sound"
class Dog(Animal):
    def speak(self):
        return "Bark!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
dog=Dog()
cat=Cat()
print(dog.speak())
print(cat.speak())

print("\n")
# Multiple Inheritance

class FlyingVehicle:
    def fly(self):
        return "This vehicle can fly"
class WaterVehicle:
    def sail(self):
        return "This vehicle can sail"
class AmphibiousCar(FlyingVehicle,WaterVehicle):
    def drive(self):
        return "This vehicle can also drive on land"
    
car=AmphibiousCar()
print(car.fly())
print(car.sail())
print(car.drive())
###
print("\n")
print(isinstance(dog,Dog))
print(isinstance(car,AmphibiousCar))
###
print(issubclass(Dog,Animal))
print(issubclass(Dog,Cat))