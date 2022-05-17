# -*- coding: utf-8 -*-
R,C,M = map(int, input().split())

board=[[0 for i in range(C)] for j in range(R)]
sharks = []
sum = 0

for i in range(M):
    info = list(map(int, input().split()))
    board[info[0]-1][info[1]-1] = i+1
    sharks.append(info)

def move_up_down(r,R,s,d):
    s %= ((R-1)*2)
    while s != 0:
        if (r == 0): d = 2
        elif (r == R - 1): d = 1

        if (d == 1): r -= 1
        else: r += 1
        s-=1

    return [r,d]

def move_left_right(c,C,s,d):
    s %= ((C-1)*2)
    while s != 0:
        if(c == 0): d = 3
        elif (c == C - 1): d = 4

        if (d == 3): c += 1
        else: c -= 1
        s-=1

    return [c,d]

for col in range(C):
    for row in range(R):
        if board[row][col] != 0 :
            sum += sharks[board[row][col]-1][4]
            del sharks[board[row][col]-1]
            break
    print(sharks)
    for i in range(len(sharks)):
        board[sharks[i][0]-1][sharks[i][1]-1] = 0

        if sharks[i][3] == 1 or sharks[i][3] == 2:
            new_info = move_up_down(sharks[i][0]-1, R , sharks[i][2] , sharks[i][3])
            sharks[i][0] = new_info[0] + 1
            sharks[i][3] = new_info[1]
        else:
            new_info = move_left_right(sharks[i][1]-1, C , sharks[i][2], sharks[i][3])
            sharks[i][1] = new_info[0] + 1
            sharks[i][3] = new_info[1]
    print(sharks)
    for i in range(len(sharks)):
        if board[sharks[i][0]-1][sharks[i][1]-1] != 0:
            exist_idx = board[sharks[i][0]-1][sharks[i][1]-1]-1
            if sharks[i][4] > sharks[exist_idx][4]:
                del sharks[exist_idx]
                board[sharks[i][0]-1][sharks[i][1]-1] = i+1
            else:
                del sharks[i]
        else:
            board[sharks[i][0]-1][sharks[i][1]-1] = i+1
    print(sharks)
    print(len(sharks))
print(sum)