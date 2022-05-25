import sys

sys.setrecursionlimit(int(1e6))


def findWorm(row, col, visited, baechu):
    row_bound = 0 <= row and row < len(baechu)
    col_bound = 0 <= col and col < len(baechu[0])
    if (not row_bound or not col_bound): return False

    pos = str(row) + ',' + str(col)
    if pos in visited: return False
    if baechu[row][col] == 0: return False
    visited.append(pos)

    findWorm(row - 1, col, visited, baechu)
    findWorm(row + 1, col, visited, baechu)
    findWorm(row, col - 1, visited, baechu)
    findWorm(row, col + 1, visited, baechu)

    return True


answer = []
T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    baechu = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        u, v = map(int, sys.stdin.readline().strip().split())
        baechu[v][u] = 1

    cnt = 0
    visited = []

    for i in range(M):
        for j in range(N):
            if baechu[j][i] == 1 and findWorm(j, i, visited, baechu):
                cnt += 1

    answer.append(cnt)

for ans in answer: print(ans)
