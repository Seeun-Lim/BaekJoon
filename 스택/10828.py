import sys

def push(stack, num):
    stack.append(num)
def pop(stack):
    if stack: print(stack.pop())
    else: print(-1)
def top(stack):
    if stack: print(stack[-1])
    else: print(-1)
def size(stack):
    print(len(stack))
def empty(stack):
    if stack: print(0)
    else: print(1)
    
N = int(sys.stdin.readline())
stack = []
for i in range(N):
    data = sys.stdin.readline().split()
    if data[0] == 'push': push(stack, data[1])
    elif data[0] == 'top': top(stack)
    elif data[0] == 'size': size(stack)
    elif data[0] == 'empty': empty(stack)
    elif data[0] == 'pop': pop(stack)

