import random
Listem=[]
def summation(myList):
    toplam=0
    for i in range(3):
        myList.append(random.randint(1,50))
        print(myList[i],end=" ")
        toplam+=myList[i]
    print("\n")
    return toplam
print(summation(Listem))    








