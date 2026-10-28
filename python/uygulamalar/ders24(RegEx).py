import re
# text="The rain in Türkiye"

# result=re.search("^The.*Türkiye$",text)
# if result:
#     print("Yes! We have a match!")
# else:
#     print("No match!")
# print(result)

# text="Hello Python 3. Regular ex is awesome!"

# result=re.findall(r"[a-m]",text)
# result1=re.findall(r"\d",text) #0-9 arası rakam
# result2=re.findall(r"P....n",text) #kaç harf varsa arada o kadar nokta konarak kelime aranır
# result3=re.findall(r"^Hel",text) # neyle başladığını yazıyoz=her satır   \A aynı işlev=tek satır
# result4=re.findall(r"!$",text) # neyle bittiğini yazıyoz
# result5=re.findall(r"Hel.*o",text) # .=herhangi bir karakter olabilir, *=0 veya daha fazla olabilir, +=en az 1 olcak
# if result:
#     print("Yes! We have a match!")
# else:
#     print("No match!")
# print(result)
# print(result1)
# print(result2)
# print(result3)
# print(result4)
# print(result5)

while True:
    name=input("Enter your name: ")
    if re.fullmatch(r"[a-zA-Z]+",name):
        print(f"Thanks! Your name is {name}")
        break
    else:
        print("R u stupid? Pls enter only letters!")