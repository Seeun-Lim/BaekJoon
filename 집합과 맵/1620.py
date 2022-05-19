import sys
N,M = map(int, sys.stdin.readline().split())

pkm = []
pokemon = {}

for i in range(N):
    sd = sys.stdin.readline().strip()
    pkm.append(sd)
    pokemon[sd] = i + 1

for i in range(M):
    s = sys.stdin.readline().rstrip()
    if s.isdigit(): print(pkm[int(s)-1])
    else:
        print(pokemon[s])
    
    