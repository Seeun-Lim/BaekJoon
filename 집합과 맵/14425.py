import sys
N, M = map(int, sys.stdin.readline().split())
cnt = 0

N_list = set([sys.stdin.readline() for _ in range(N)])
    
for i in range(M):
    s = sys.stdin.readline()
    if s in N_list: cnt+=1
    
print(cnt)
    
