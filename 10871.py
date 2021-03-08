import sys
N,X=map(int,sys.stdin.readline().split())

data=list(map(int,sys.stdin.readline().split()))

for i in data:
    if(i<X):
        print(i,end=' ')