# class BankAccount:
#     def __init__(self,account_number,balance):
#         self.account_number=account_number
#         self.__balance=balance
#     def deposit(self,amount):
#         if(amount>0):
#             self.__balance+=amount
#             return f"Deposited:${amount} New Balance:${self.__balance}"
#         return "Invalid deposit amount!"
#     def __display_balance(self):
#         return f"Balance:${self.__balance}"
#     def get_balance(self):
#         return self.__display_balance()
    
# account=BankAccount("12345678",2000)
# print(account.account_number)
# print(account._BankAccount__balance)
# print(account.deposit(50))

class Employee:
    def __init__(self,name,salary):
        self.name=name  #public
        self._bonus=700 #protected
        self.__salary=salary    #private

        def _calculateBonus(self):
            return self._bonus
        def __calculateSalary(self):
            return f"Salary:${self.__salary}"
        def getSalaryInfo(self):
            return self.__calculateSalary()

class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department=department

    def displayInfo(self):
        return f"Manager:{self.name}, Department:{self.department}, Bonus:${self._bonus}"
    
manager=Manager("Emir",2000,"IT")
print(manager.displayInfo()) 