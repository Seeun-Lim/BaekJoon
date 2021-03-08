N=int(input())
count=0

def HANnumber(n):
    d=[]
    while True:
        d.append(n%10)
        if (n < 10): break
        n//=10
    diff=d[1]-d[0]
    for i in range(1,len(d)-1):
        if (d[i+1]-d[i])!=diff:
            return False
    return True

for i in range(1,N+1):
    if(i<10): count+=1
    else:
        if(HANnumber(i)): count+=1

print(count)