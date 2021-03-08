def isExist(a,b):
    for i in range(len(a)):
        if(a[i][0]==b):
            return i
            break
    return -1

word=input()
word=word.upper()
result=[]

for i in range(len(word)):
    if isExist(result,word[i])==-1:
        result.append([word[i],1])
    else:
        index=isExist(result,word[i])
        result[index][1]+=1

max=result[0][1]
max_index=-1

for i in range(len(result)):
    if result[i][1]>=max:
        max=result[i][1]
        max_index=i

flag=1

for i in range(len(result)):
    if result[i][1]==max:
        if max_index!=i:
            flag=0
            break

if flag==0:
    print("?")
else:
    print(result[max_index][0])
