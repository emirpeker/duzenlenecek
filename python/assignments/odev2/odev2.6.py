text="Welcome to 'Introduction to Python'!"
vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
count=0
for i in range(len(text)):
    letter=text[i]
    for j in range(len(vowels)):
        if(letter==vowels[j]):
            count+=1
            break
print("Sesli harf sayisi:",count)