# class Student():
#     def __init__(self,name):
#         self.name=name
#         self.points=[]

#     def add_grade(self,grade):
#         self.points.append(grade)

#     def average(self):
#         sum=0
#         for i in self.points:
#             sum+=i
#         average=(sum/len(self.points))
#         return average
# st1=Student("Emir")

# st1.add_grade(70)
# st1.add_grade(80)
# st1.add_grade(60)
# avg=st1.average()

# print("Öğrenci:",st1.name)
# print("Ortalama:",avg)
# if avg>60:
#     print("Durum:Geçti")
# else:
#     print("Durum:Kaldı")

# class Task():
#     def __init__(self, name, minutes):
#         self.name = name
#         self.minutes = minutes
#         self.completed = False

# class TaskManager():
#     def __init__(self):
#         self.tasks = []

#     def add_task(self, task):
#         self.tasks.append(task)

#     def complete_task(self, task_name):
#         for task in self.tasks:
#             if task.name == task_name: 
#                 task.completed = True
#                 print(f"Görev tamamlandı: {task.name}")
#                 return

#     def total_time(self):
#         total = 0
#         for task in self.tasks:
#             total += task.minutes
#         return total

#     def completed_count_recursive(self,i=0):
#         if i==len(self.tasks):

#             return 0
#         current_task=self.tasks[i]
#         count=0
#         if current_task.completed:
#             count=1
#         return count+self.completed_count_recursive(i+1)
# manager = TaskManager()

# gorev1 = Task("Ders Çalış", 50)
# gorev2 = Task("Yemek Ye", 30)

# manager.add_task(gorev1)
# manager.add_task(gorev2)

# manager.complete_task("Ders Çalış")
# print("Toplam Süre:", manager.total_time())
# print("Tamamlanan Görev Sayısı:", manager.completed_count_recursive())


def basamak_toplami(number):
    if number==0:
        return 0
    return (number%10)+basamak_toplami(number//10)

def cift_toplamlari_say(n):
    sayac=0
    for i in range(1,n+1):
        toplam=basamak_toplami(i)

        if toplam%2==0:
            sayac+=1
    return sayac
try:
    number=int(input("Please enter a positive number:"))
    if number>0:
        sonuc = cift_toplamlari_say(number)
        print(f"1'den {number}'e kadar rakamları toplamı ÇİFT olan sayı adedi: {sonuc}")
    else:
        print("Invalid number!")
except ValueError:
    print("Invalid number!")