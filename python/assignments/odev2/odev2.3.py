yazi=["Ahmet","alti","yasinda","zeynep","dort","yasinda","esra","iki","yasinda","ayse","bir","yasinda"]
numbers={"bir":"1","iki":"2","dort":"4","alti":"6"}
newYazi=[]
for i in range(len(yazi)):
    word=yazi[i]
    if (word in numbers):
        newYazi.append(numbers[word])
    else:
        newYazi.append(word)
output=""
for i in range(len(newYazi)):
    output+=newYazi[i]+" "
print("Output=",output.strip())