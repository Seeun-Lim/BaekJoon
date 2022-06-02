import heapq
import sys

N = int(sys.stdin.readline())
arr = []

for i in range(N):
    x = int(input())
    if x == 0:
        if arr:
            print(heapq.heappop(arr)[1])
        else:
            print(0)
    else:
        heapq.heappush(arr, (-x, x))

