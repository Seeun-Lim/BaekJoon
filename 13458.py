import math

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

judges = [0 for i in range(N)] 

for i in range(N):
    while A[i] > 0:
        if judges[i] == 0:
            judges[i] +=1
            A[i] = A[i] - B
        else:
            judges[i] += math.ceil(A[i]/C)
            A[i] -= math.ceil(A[i]/C)*C

print(sum(judges))