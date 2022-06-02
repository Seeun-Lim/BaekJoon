import sys
from collections import deque

T = int(sys.stdin.readline())

def BFS(src, dst):
    q = deque()
    q.append(src)
    while q:
        current = q.popleft()



for _ in range(T):
    X = int(sys.stdin.readline())
    src_x, src_y = map(int, sys.stdin.readline().split())
    dst_x, dst_y = map(int, sys.stdin.readline().split())

    BFS([src_x, src_y], [dst_x, dst_y])
