word=input()
data=[]

for i in range(26):
    data.append(-1)

for i in range(len(word)):
    a=int(ord(word[i])-97)
    if data[a]==-1:
        data[a]=i

for i in data:
    print(i,end=' ')