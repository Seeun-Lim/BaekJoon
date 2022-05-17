import sys

V = int(sys.stdin.readline())
E = int(sys.stdin.readline())
network = [[] for _ in range(V)]

for i in range(E):
    u,v = map(int, sys.stdin.readline().split())
    network[v-1].append(u)
    network[u-1].append(v)

cnt = 0
visited = [0] * V

def dfs(start):
    visited[start] = 1
    for computer in network[start]:
        if not visited[computer-1]: dfs(computer-1)
    
dfs(0)

print(visited.count(1)-1)