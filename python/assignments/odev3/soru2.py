import random

def manuel_sort(liste):
    n=len(liste)
    for i in range(n):
        max_index=i
        for j in range(i+1,n):
            if liste[j]>liste[max_index]:
                max_index=j
        liste[i],liste[max_index]=liste[max_index], liste[i]
    return liste

liste1=[random.randint(1,100) for i in range(5)]
liste2=[random.randint(1,100) for i in range(5)]
print("Liste 1:",liste1)
print("Liste 2:",liste2)
merged=liste1+liste2
sorted=manuel_sort(merged)
print("Buyukten kucuge sirali hali: ",sorted)