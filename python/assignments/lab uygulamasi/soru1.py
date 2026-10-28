text=input("Lutfen metni gir: ")
metin=text.lower()
noktalamaIsaretleri='.,;:!?()"\'[]{}<>'

for isaret in noktalamaIsaretleri:
    metin=metin.replace(isaret,"")

kelimeler=metin.split()
arr={}
for kelime in kelimeler:
    if kelime in arr:
        arr[kelime]+=1
    else:
        arr[kelime]=1
print(arr)