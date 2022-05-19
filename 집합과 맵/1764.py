import sys

N,M = map(int, sys.stdin.readline().split())
hear = set([sys.stdin.readline() for _ in range(N)])
see = set([sys.stdin.readline() for _ in range(M)])

seeHear = list(hear&see)
seeHear.sort()

print(len(seeHear))
for person in seeHear: 
    print(person, end='')