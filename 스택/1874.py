import sys
input = sys.stdin.readline

n = int(input())
goal_stack = [int(input().strip()) for i in range(n)]
    
stack=[]
answer = []
i = 1
flag = 0

for item in goal_stack:
    if flag == 1: break
    
    while True:
        if i > item or i > n:
            if stack and stack[-1] == item:
                stack.pop()
                answer.append('-')
            else: flag=1
            break
        else:
            stack.append(i)
            answer.append('+')
            i+=1
    
if flag == 1: print('NO')
else: 
    for item in answer:
        print(item)