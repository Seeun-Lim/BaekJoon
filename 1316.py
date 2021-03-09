def isExist(group,ch):
    for i in range(len(group)):
        if group[i]==ch:
            return True
            break
    return False

def isGroupNum(word):
    group=[]
    for i in range(len(word)):
        if isExist(group,word[i])==False:
            group.append(word[i])
        else:
            if i!=0 and word[i-1] == word[i]:
                continue
            else:
                return False
    return True

N=int(input())
count=0

for i in range(N):
    word=input()
    if isGroupNum(word)==True:
        count+=1
print(count)