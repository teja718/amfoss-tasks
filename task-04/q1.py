r1=int(input())
a=list(map(int,input().split()))
r2=int(input())
b=list(map(int,input().split()))
c=[]
for i in b:
    if i not in a:
        c.append(i)       
f1={}
for num in a:
    if num in f1:
        f1[num]+=1
    else:
        f1[num]=1
print(f1)        
f2={}
for num in b:
    if num in f2:
        f2[num]+=1
    else:
        f2[num]=1
print(f2)
for i in f2:
    for i in f1:
        if f2[i]!=f1[i]:
            c.append(i)     
            f1[i]=f1[i]+1

for i in c :
    print(c[i],end=" ")