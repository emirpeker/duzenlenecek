list=[2, 2, 3, 3, 8, 8, 9, 1, 1, 5, 4, 4]
newList=[]
for i in range(len(list)):
    item=list[i]
    if(list.count(item)==1):
            newList.append(item)
print("Yeni liste:",newList,end=" ")