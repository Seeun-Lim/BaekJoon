def howmany(k,n):
    apart=[[]]
    total = 0
    for i in range(1,n+1):
        apart[0].append(i)
    sum=0
    if k==1:
        for j in range(n):
            sum += apart[0][j]
        print(sum)
    else:
        for i in range(1,k):
            data=[]
            sum=0
            for j in range(n):
                sum+=apart[i-1][j]
                total+=sum
                data.append(sum)
            apart.append(data)
        print(total)

T=int(input())

for i in range(T):
    k=int(input())
    n=int(input())
    howmany(k,n)