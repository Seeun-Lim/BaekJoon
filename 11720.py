N=int(input())
data=int(input())
sum=0
for i in range(N):
    sum+=(data%10)
    data//=10
print(sum)