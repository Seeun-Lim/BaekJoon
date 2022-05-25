import sys

N, M = map(int, sys.stdin.readline().strip().split())

def findPath(row, col, dst, visited, arr):
    r_bound = 0 <= row and row < N
    c_bound = 0 <= col and col < M
    if not r_bound or not c_bound:
        return 0

    if arr[row][col] == 0:
        return 0

    position = str(row) + ',' + str(col)
    if position in visited:
        return 0
    visited[position] = 0

    size = 1
    size += findPath(row-1, col, dst, visited, arr)
    size += findPath(row+1, col, dst, visited, arr)
    size += findPath(row, col-1, dst, visited, arr)
    size += findPath(row, col+1, dst, visited, arr)

    return size





miro=[ list(sys.stdin.readline().strip()) for _ in range(N)]

dst = str(N-1)+','+str(M-1)

print(findPath(0, 0, dst, {}, miro))