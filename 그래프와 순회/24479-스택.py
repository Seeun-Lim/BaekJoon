import sys

V, E, start = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(V)]

for i in range(E):
    u, v = map(int, sys.stdin.readline().split())
    graph[u-1].append(v)
    graph[v-1].append(u)
    
for i in range(V):
    graph[i] = sorted(graph[i], reverse=True)
    
print(graph)
    
stack = [start-1]
order = 1
visited = [0 for _ in range(V)]

while stack:
    current_node = stack.pop()
    if visited[current_node]: continue
    visited[current_node] = order
    order += 1
    
    for neighbor in graph[current_node]:
        if not visited[neighbor-1]: 
            stack.append(neighbor-1)

for i in range( len(visited)):
    print(visited[i])
    

