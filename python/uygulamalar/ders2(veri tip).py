name="Emir" #str
age=19 #int
weight=71.2 #float
comp=2j #complex

myList=["Apple","Grape","Cherry","Watermelon","Lemon","Banana"]
myTuple=("Red","Blue","White","Black","Pink","Orange") #listeye dönüşmeden değiştirilemez!
x=list(myTuple)
myRange=range(7) #range data type 0-6
myDict={"name":"Emir","age":19} #dict data type // key-value
mySet={"Apple","Grape","Cherry","Watermelon","Lemon","Banana"} #set data type
myFrozen=frozenset({"Red","Blue","White","Black","Pink","Orange"})

myBool=True #boolean
mynone=None #NULL

import sys
x=7
print(sys.getsizeof(x))

namee=b"python" #bytes 01001
myBytearray=bytearray([65]) #bytearray
myMemoryView=memoryview(bytes(5))
print(type(myMemoryView))
print(myMemoryView)

print(type(mynone))
print(mynone)


#print("isim:",name,"yas:",age,"kilo:",weight,"karmasik sayi:",comp)
#print("isim:"+name+"yas:"+str(age)+"kilo:"+str(weight)+"karmasik sayi:"+str(comp))