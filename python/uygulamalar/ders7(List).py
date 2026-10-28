#Kullanicidan alinan 7 sayiyi siralayip yazdiran program
""" myNumbers=[]
i=0
while i<7:
    input_number=int(input("Enter an integer: "))
    myNumbers.append(input_number)
    i+=1
myNumbers.sort()
print(myNumbers)
"""
#Girilen sayiya kadar olan tek ve cift sayilari yazdiran program
startNumber=int(input("Enter the start number: "))
endNumber=int(input("Enter the ending number: "))

while startNumber<endNumber:
    if startNumber%2==0:
        print(startNumber,end=" ")
    startNumber+=1