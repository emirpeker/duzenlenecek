text=input("Bir cumle giriniz: ")
word=""
longest=""
for i in range(len(text)):
    if (text[i]!=" "):
        word+=text[i]
    else:
        if (len(word)>len(longest)):
            longest=word
        word=""
if(len(word)>len(longest)):
    longest=word
print("Cumledeki en uzun kelime:",longest)