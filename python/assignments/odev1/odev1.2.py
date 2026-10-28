import random
newList=[random.randint(1,25) for _ in range(20)]
print("Liste: ",newList)
sum=0
index=-1

for i in range(len(newList)):
    sum+=newList[i]
    if sum>100:
        index=i
        break
if index!=-1:
    print(f"Toplam 100 u gecti! {index+1}.eleman ({newList[index]}) eklendiğinde toplam {sum} oldu.")
else:
    print("Toplam 100'e ulasmadigi icin tüm elemanlar toplandi:", sum)