N=int(input())
cycle=0
origin=N

while True:
    cycle+=1

    a=N%10
    b=(N//10+N%10)%10
    N=a*10+b

    if N == origin:
        break

print(cycle)
