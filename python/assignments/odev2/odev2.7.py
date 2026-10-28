import random
numbers=[]
for i in range(5):
    numbers.append(random.randint(1,100))
print(numbers,end=" ",)
max=numbers[0]
for i in range(1,len(numbers)):
    if(numbers[i]>max):
        max=numbers[i]
second=0
for i in range(len(numbers)):
    if (numbers[i]!=max):
        if(second==0) or (numbers[i]>second):
            second=numbers[i]
print("\nIkinci en buyuk sayi: ",second)