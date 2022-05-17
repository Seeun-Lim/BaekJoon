import sys

def isVPS(stack):
    vps_stack=[]
    if stack.pop() == '(': return 'NO'
    else: vps_stack.append(')')
    
    while stack:
        if stack.pop()=='(': 
            if vps_stack: vps_stack.pop()
            else: return 'NO'
        else: vps_stack.append(')')
    
    if len(vps_stack) == 0: return 'YES'
    else: return 'NO'

N = int(sys.stdin.readline())
for i in range(N):
    stack=list(map(str, sys.stdin.readline().strip()))
    print(isVPS(stack))
    