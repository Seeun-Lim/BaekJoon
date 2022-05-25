import sys
from collections import deque

M, N = map(int, sys.stdin.readline().strip().split())
tomato = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

q = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append([i, j])

def BFS():
    while q:
        row, col = q.popleft()
        for i in range(4):
            nx, ny = dx[i] + row, dy[i] + col
            if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[row][col] + 1
                q.append([nx, ny])

BFS()
cnt = 0

for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    cnt = max(cnt, max(i))

print(cnt - 1)