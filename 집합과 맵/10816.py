import sys
N = int(sys.stdin.readline())
card = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))

card.sort()
card_dict={}

for item in card:
    if item not in card_dict: card_dict[item] = 0
    card_dict[item] += 1

for item in num:
    if item in card_dict: print(card_dict[item], end=' ')
    else: print(0, end=' ')
