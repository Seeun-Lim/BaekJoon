import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
miro = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

q = deque([])
q.append([0, 0])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[0, 0]]

def BFS():
    while q:
        row, col = q.popleft()
        for i in range(4):
            nx, ny = dx[i] + row, dy[i] + col
            if 0 <= nx < N and 0 <= ny < M and miro[nx][ny] == 1 and [nx, ny] not in visited:
                miro[nx][ny] = miro[row][col] + 1
                q.append([nx, ny])
    return miro[N-1][M-1]
print(BFS())

