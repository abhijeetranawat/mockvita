lst=sorted(list(map(int,input().split())),reverse=True)
lst1=[]
lst2=[]
lst1.append(lst[0])
lst.pop(0)
lst2.append(lst[0])
lst.pop(0)
for i in range(len(lst)):
    if(sum(lst1)>sum(lst2)):
        lst2.append(lst[0])
        lst.pop(0)
    else:
        lst1.append(lst[0])
        lst.pop(0)
print(max(sum(lst1),sum(lst2)))
