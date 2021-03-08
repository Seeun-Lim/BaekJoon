N=int(input())
for i in range(N):
    data=input()
    index=0
    length=len(data)
    score=total=0
    while True:
        if index==length:
            break
        if data[index]=='O':
            score+=1
        else:
            score=0
        total+=score
        index+=1
    print(total)
