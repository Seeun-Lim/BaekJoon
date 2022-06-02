import heapq
import sys

N = int(sys.stdin.readline().strip())
arr = []

for i in range(N):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(arr, (x, 1))
    elif x < 0:
        heapq.heappush(arr, (-x, 0))
    else:
        if arr:
            item = heapq.heappop(arr)
            if item[1] == 1:
                print(item[0])
            else:
                print(-item[0])
        else:
            print(0)
