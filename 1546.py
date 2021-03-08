import sys
N=int(input())

score=list(map(int,sys.stdin.readline().split()))
max=score[0]
for i in score:
    if(i>max):
        max=i
avg=0
for i in score:
    i=i/max*100
    avg+=i

print("%.1f"%(avg/N))