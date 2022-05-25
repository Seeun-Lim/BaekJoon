import sys

N = int(sys.stdin.readline())
map = [list(map(int, sys.stdin.readline().strip())) for i in range(N)]


def findHouse(row, col, visited):
    row_bound = 0 <= row and row < N
    col_bound = 0 <= col and col < N
    if (not row_bound or not col_bound): return False

    if map[row][col] == 0: return False

    position = str(row) + ',' + str(col)
    if position in visited: return False
    visited.append(position)

    findHouse(row - 1, col, visited)
    findHouse(row + 1, col, visited)
    findHouse(row, col - 1, visited)
    findHouse(row, col + 1, visited)

    return visited


answer = [0]
visited = []
first = 0

for i in range(N):
    for j in range(N):
        if map[i][j] == 1:
            return_list = findHouse(i, j, visited)
            if return_list:
                answer.append(len(return_list) - sum(answer))

print(len(answer) - 1)
answer.sort()
for i in range(1, len(answer)): print(answer[i])