import sys

A = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

answer = [-1] * A
stack = []

for i in range(A):
    while stack and stack[-1][0] < data[i]:
        e = stack.pop()
        answer[e[1]] = data[i]
    stack.append([data[i],i])

for i in answer:
    print(i, end=' ')