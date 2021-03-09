N=int(input())

first=1
index=1
count=0

while N>=first:
    first+=index
    index+=1
    count+=1

bottom=first-N
up=count-first+1+N
if count%2==1:
    print(bottom,'/',up,sep='')
else:
    print(up, '/', bottom, sep='')