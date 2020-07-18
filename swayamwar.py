n=int(input())
lst1=list(input())
lst2=list(input())
r=0
m=0
flag=0
for el in lst2:
    if(el=='r'):
        r+=1
    else:
        m+=1
for i in range(n):
    if(lst1[i]=="m"):
        if(m>0):
            m-=1
        else:
            flag = 1
            break
    else:
        if (r > 0):
            r -= 1
        else:
            flag = 1
            break
print(n-i-1+flag)
