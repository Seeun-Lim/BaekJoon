import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == '.': break
    
    isVPS = 'yes'
    stack=[]
    
    for item in s:
        if item == '(' or item == '[': stack.append(item)
        elif item == ')': 
            if stack and stack[-1] == '(': stack.pop()
            else: 
                isVPS = 'no'
                break
        elif item == ']': 
            if stack and stack[-1] == '[': stack.pop()
            else: 
                isVPS = 'no'
                break
    if(len(stack) != 0): isVPS='no'
    print(isVPS)
            