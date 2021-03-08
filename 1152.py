data=input()

count=0

for i in range(len(data)):
    if i==0 and data[i]!=" ":
        count+=1
    else:
        if data[i-1]==" " and data[i]!=" ":
            count+=1

print(count)