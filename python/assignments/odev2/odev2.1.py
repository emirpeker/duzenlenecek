import random
array1=[]
array2=[]
merged=[]
result=[]
for i in range(10):
    array1.append(random.randint(1,50))
    array2.append(random.randint(1,50))
print("1.Dizi: ",array1,end=" ")
print("\n2.Dizi: ",array2,end=" ")    

for i in range(len(array1)):
    merged.append(array1[i])
for i in range(len(array2)):
    merged.append(array2[i])

for i in range(len(merged)):
    count=0
    for j in range(len(merged)):
        if(merged[i]==merged[j]):
            count+=1
    if(count==1):
        result.append(merged[i])

for i in range(len(result)):
    for j in range(i+1,len(result)):
        if(result[i]>result[j]):
            temp=result[i]
            result[i]=result[j]
            result[j]=temp
print("\nDizilerin son hali: ",result)