import sys
sys.setrecursionlimit(int(1e6))
    
V, E, start = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(V+1)]

for i in range(E):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(1,V+1):
    graph[i] = sorted(graph[i])

visited = [0] * (V+1)

def dfs(start):
    global no
    visited[start] = no
    no += 1
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(neighbor)
    
no = 1
dfs(start)

for i in range(1,V+1): print(visited[i])