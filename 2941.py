def isExist(group,ch):
    for i in group:
        if i==ch:
            return False
    return True

def isGroupWord(a):
    group=[]
    print("isgroup")
    for i in range(len(a)):
        if i!=len(a)-1 and a[i]==a[i+1]:
            print("Okay")
            continue
        else:
            if isExist(group,a[i])==True:
                print("detect")
                return False
                break
            else:
                print("Append")
                group.append(a[i])

N=int(input())
count=0

for i in range(N):
    word=input()
    if isGroupWord(word):
        count+=1
print(count)