class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def myPrint(self):
        print(self.firstname,self.lastname)
class IdariPersonel(Person):
    ...
class AkademikPersonel(Person):
    ...

class Student(Person):
    def __init__(self, fname, lname,year):
        super().__init__(fname,lname)
        self.graduationyear=year
    def welcome(self):
        print(f"Welcome {self.firstname} {self.lastname} to the class of {self.graduationyear}")

p1=Person("Emir","Peker")
p2=Student("Isim","Soyisim",2025)
p1.myPrint()
p2.myPrint()
print(p2.graduationyear)
p2.welcome()