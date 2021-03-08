import sys

N=int(input())
data=list(map(int,sys.stdin.readline().split()))
min=max=data[0]

for i in range(1,N):
    if(data[i]<min): min=data[i]
    if(data[i]>max): max=data[i]

print(min,max)