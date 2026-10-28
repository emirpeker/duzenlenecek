fruits=("strawberry","grape","pineapple","cherry","melon","watermelon")
fruits1=("strawberry",) #tuple
fruits2=("grape") #str
complex_Tuple=("Fehmi",34,True,"Seyda",36,False)

print(fruits)
print(len(fruits))
print(complex_Tuple)

#ögelere erişim

print(fruits[0])
print(fruits[1:5])

search="grape"
if(search in fruits):
    print(f"yes, '{search}' is in the fruits tuple")
else:
    print(f"no, '{search}' is not in the fruits tuple")    

numbers=(7,19,23,4)
joinTuple=numbers+fruits
multiplyFruits=fruits*2
print(joinTuple)

#Tuple güncelleme

temp_fruits=list(fruits)
temp_fruits[2]="lemon"

fruits=tuple(temp_fruits)
print(fruits)

(x,*y,z)=fruits
print(x)
print(y)

