Liste=[1,2,3,3,4,6,8,9,8,1,2,5,4,3]
newList=[]
itemsList=[]
for i in range(len(Liste)):
    item=Liste[i]
    exist=0
    for j in range(len(itemsList)):
        if(itemsList[j]==item):
            exist=1
            break
    if(exist==0):
        count=Liste.count(item)
        if(count>1):
            print(f"{item} elemanindan {count} kadar var, tekrarlar silinecek..")
        itemsList.append(item)
        if(count==1):
            newList.append(item)
print("Yeni liste:",newList,end=" ")

