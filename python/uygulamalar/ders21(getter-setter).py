# CLASS METHODS

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     @classmethod
#     def birth_year(cls,name,birth_year):
#         current_year=2025
#         calculated_age=current_year-birth_year
#         return cls(name,calculated_age)

#     def display_info(self):
#         return f"{self.name} is {self.age} years old"

# p1=Person.birth_year("Emir",2006)
# print(p1.display_info())
#-----------------------------------------------------
# class Employee:
#     company="GoogleCop"
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

#     @classmethod
#     def set_company(cls,new_company):
#         cls.company=new_company
    
#     @classmethod
#     def get_value(cls,name,salary):
#         return cls(name,int(salary))
    
#     def display_info(self):
#         return f"Employee: {self.name}\nSalary: {self.salary}\nCompany: {self.company}"
    
# emp1=Employee.get_value("Emir PEKER",4000)
# print(emp1.display_info())

#-------------------
# GETTER,SETTER,DELETER
class Person:
    def __init__(self,name):
        self._name=name

    @property
    def name_function(self):  #getter
        return self._name
    
    @name_function.setter
    def name_function(self,new_name):
        if not new_name:
            raise ValueError("Name cannot be empty!")
        self._name=new_name
    
    @name_function.deleter
    def name_function(self):
        print("Deleting name variable...")
        self._name=None
p1=Person("Emir PEKER")
print(p1.name_function)
p1.name_function="Burak PEKER"
print(p1.name_function)
del p1.name_function
print(p1.name_function)