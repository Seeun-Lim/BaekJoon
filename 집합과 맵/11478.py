import sys

str = sys.stdin.readline().strip()
print(sum(len({str[i:i+gap] for i in range(len(str)+1-gap)}) for gap in range(1, len(str)+1)))    