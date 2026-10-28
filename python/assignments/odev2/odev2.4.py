list=[1, 2, 3, 1, 2, 3, 4, 5, 6, 5, 6, 7, 8]
longest=[]
sublist=[list[0]]
for i in range(1,len(list)):
    if (list[i]>list[i-1]):
        sublist.append(list[i])
    else:
        if(len(sublist)>len(longest)):
            longest=[]
            for j in sublist:
                longest.append(j)
        sublist=[list[i]]

if(len(sublist)>len(longest)):
    longest=[]
    for i in sublist:
        longest.append(i)
print("En uzun artan ardisik alt dizi:",longest,end=" ")