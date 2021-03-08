arr=[]
for i in range(42):
    arr.append(0)

for i in range(10):
    N=int(input())
    arr[N%42]+=1

count=0
for i in arr:
    if i!=0:
        count+=1

print(count)

