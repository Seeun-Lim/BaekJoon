import sys
C=int(input())

for i in range(C):
    data=list(map(int,sys.stdin.readline().split()))
    size=len(data)
    index=1
    N=data[0]
    avg=0
    while index!=size:
        avg+=data[index]
        index+=1
    avg/=N
    avg_student=0
    for j in range(1,size):
        if(avg<data[j]):
            avg_student+=1
    percent=(avg_student/N)*100
    print("%.3f"%percent+"%")
