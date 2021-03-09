A,B,C=map(int,input().split())

if (C-B)!=0:
    point=int(A/(C-B))
    if point < 0:
        print("-1")
    else:
        print(point + 1)
else:
    print("-1")
