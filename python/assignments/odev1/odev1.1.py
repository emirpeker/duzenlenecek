newList=[]
print("10 elemanli listeyi doldurun:")
while len(newList)<10:
    num=int(input(f"{len(newList)+1}. sayiyi gir: "))
    if not newList:
        newList.append(num)
    else:
        if num>newList[-1]:
            newList.append(num)
        else:
            print("Bu sayi onceki sayidan kucuk!")
print("\nDüz liste:")
for i in newList:
    print(i, end=" ")
print("\nTers siralanmis liste: ")
for i in reversed(newList):
    print(i,end=" ")    