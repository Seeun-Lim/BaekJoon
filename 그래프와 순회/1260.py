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
     
dfs_visited = []
def dfs(start):
    dfs_visited.append(start)
    for neighbor in graph[start]:
        if neighbor-1 not in dfs_visited:
            dfs(neighbor-1)

bfs_visited = []

def bfs(start):
    q = Queue()
    q.put(start)
    
    while not q.empty():
        current_node = q.get()
        if current_node in bfs_visited: continue
        bfs_visited.append(current_node)
        for neighbor in graph[current_node]:
            if neighbor-1 not in bfs_visited:
                q.put(neighbor-1)
            

dfs(start-1)
bfs(start-1)

for i in list(map(lambda x:x+1,dfs_visited)):
    print(i, end=' ')
print()

for i in list(map(lambda x:x+1,bfs_visited)):
    print(i, end=' ')