import sys
N = int(sys.stdin.readline())
card = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))

card.sort()

def binarySearch(start, end, target):
    if start > end: return 0
    
    middle = (start+end)//2    
    if card[middle] == target: return 1
    elif card[middle] > target: return binarySearch(start, middle-1, target)
    elif card[middle] < target: return binarySearch(middle+1, end, target)

for target in num:
    print(binarySearch(0, len(card)-1, target), end=' ')
    