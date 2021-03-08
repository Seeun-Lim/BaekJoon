A=int(input())
B=int(input())
C=int(input())

mul=A*B*C
result=[0,0,0,0,0,0,0,0,0,0]

while True:
    result[mul%10]+=1
    if (mul < 10):
        break
    mul//=10

for i in result:
    print(i)