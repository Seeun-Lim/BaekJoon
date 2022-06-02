import heapq
import sys

N = int(sys.stdin.readline())
arr = []

for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if arr:
            print(heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, x)