class CustomList:
    def __init__(self,items):
        self.items=items
    def __len__(self):
        return len(self.items)
my_list=CustomList([1,7,19,12,5,2])
print(len(my_list))

class Greet:
    def __call__(self, name):
        return f"Hello ,{name}!"
greet=Greet()
print(greet("Emir Peker"))

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __eq__(self, other):
        return self.age==other.age
    def __lt__(self,other):
        return self.age<other.age
    def __le__(self,other):
        return self.age<=other.age
    def __gt__(self,other):
        return self.age>other.age
    def __ge__(self,other):
        return self.age>=other.age
    def __ne__(self, other):
        return self.age!=other.age
p1=Person("Emir",19)
p2=Person("John",23)
print(p1==p2)
print(p1<p2)
print(p1<=p2)
print(p1>p2)
print(p1>=p2)
print(p1!=p2)