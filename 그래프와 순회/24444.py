import sys
from queue import Queue

V,E,start = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(V)]
for i in range(E):
    u,v = map(int, sys.stdin.readline().split())
    graph[u-1].append(v)
    graph[v-1].append(u)
for i in range(V):
    graph[i] = sorted(graph[i])

order = 1
visited = [0] * V
q = Queue()
q.put(start-1)

while not q.empty():
    current_node = q.get()
    if visited[current_node]: continue
    visited[current_node] = order
    order += 1
    
    for neighbor in graph[current_node]:
        if not visited[neighbor-1]:
            q.put(neighbor-1)
            
for item in visited: print(item)
    




    




