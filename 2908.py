def Sangsue(a):
    newnum=0
    index=2
    while True:
        newnum+=((10**index)*(a%10))
        if a<10:
            break
        a//=10
        index-=1
    return newnum

A,B=map(int,input().split())

print(max(Sangsue(A),Sangsue(B)))
