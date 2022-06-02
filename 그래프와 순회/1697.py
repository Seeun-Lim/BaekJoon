import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split())

MAX = 100000
cnt = [0] * (MAX + 1)

q = deque()
q.append(N)

while q:
    x = q.popleft()
    if x == K:
        print(cnt[x])
        break
    for dx in (x+1, x-1, x*2):
        if 0 <= dx < MAX+1 and cnt[dx] == 0:
            cnt[dx] = cnt[x] + 1
            q.append(dx)