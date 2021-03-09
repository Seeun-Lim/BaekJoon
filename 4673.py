def d(n):
    newnum=n
    while True:
        newnum+=(n%10)
        if n<10: break
        n//=10
    return newnum

group=[]

for i in range(10001):
    group.append(i)

for i in range(10001):
    newnum=d(i)
    if newnum<10001:
        group[newnum]=-1

for i in group:
    if i!=-1:
        print(i)