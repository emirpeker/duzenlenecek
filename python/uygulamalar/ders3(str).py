print("It's alright!")
print("He is called 'big boy'")
print('He is called \'big boy\'') 
text="""
        This is multiline strings
        aaaa
        eeee

"""
print(text)
print("is" in text)
print("emir" in text)
metin="The best language in life are free!"
search="expensive"

if search not in metin:
    print("No, 'expensive' is not present!")
#dilimleme
yazi=" Python is, Weird"
print(yazi[1:5])
result=metin +" "+ yazi
print(result)

#fonksiyonlar
print(yazi.upper())#upper case 
print(yazi.lower())#lower case 
print(yazi.strip())# boşlukları kaldırıyo
print(yazi.replace("P","T"))
ayir=yazi.split(",")
print(ayir)

#str formatlama
age=19
name="Emir"
text1="My name is {0}, I am {1}".format(name,age)
text1=f"My name is {name}, I am {age}" #f-string
print(text1)