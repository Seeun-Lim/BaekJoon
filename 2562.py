max=0
max_index=0

for i in range(9):
    N=int(input())
    if N>max:
        max=N
        max_index=i

print(max)
print(max_index+1)
