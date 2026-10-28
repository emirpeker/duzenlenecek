x1 = int(input("x1 değerini gir: "))
y1=int(input("y1 değerini gir: "))
x2=int(input("x2 değerini gir: "))
y2=int(input("y2 değerini gir: "))

if x2-x1==0:
    print("Eğim tanimsizdir!")
else:
    m=(y2-y1)/(x2-x1)
    print("eğim: ",m)