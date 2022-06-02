import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().strip().split())
tomato = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N*H)]

q = deque([])
dx, dy, dz = [1, -1, 0, 0], [0, 0, 1, -1], [-N, N, 0, 0]

for i in range(N*H):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append([i, j])

def print_tomato():
    print('------')
    for i in tomato:
        for j in i:
            print(j, end=' ')
        print()

def BFS():
    while q:
        x, y = q.popleft()
        for i in range(4):
            print_tomato()
            nx, ny, nz = dx[i] + x, dy[i] + y, dz[i] + x
            if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                q.append([nx, ny])
            if i > 1:
                continue
            elif 0 <= nz < N*H and tomato[nz][y] == 0:
                tomato[nz][y] = tomato[x][y] + 1
                q.append([nz, y])

BFS()
print(tomato)

