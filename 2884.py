H,M=map(int,input().split())

if H==0 and M<45:
    H=24
if M<45:
    M+=60
    H-=1

print(H,M-45)