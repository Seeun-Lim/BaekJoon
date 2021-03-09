def roomAssign(H,W,N):
    index=flag=0
    for i in range(1,W+1):
        for j in range(1,H+1):
            index+=1
            if index==N:
                flag=1
                break
        if flag==1:
            break
    roomnumber=j*100+i
    print(roomnumber)

T=int(input())
for i in range(T):
    H,W,N=map(int,input().split())
    roomAssign(H,W,N)
