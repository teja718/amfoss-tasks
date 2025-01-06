=int(input())
l1=list(map(int,input().split()))
f1={}
for num in l1: 
    if num in f1:
        f1[num]+=1
    else:
        f1[num]=1
for i in f1:
    if f1[i]==1:
        print(i,end=" ")        
