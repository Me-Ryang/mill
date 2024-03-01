import sys
from collections import Counter

N = int(input())
cards = Counter(list(map(int, sys.stdin.readline().split())))
M = int(input())
cnt = list(map(int, sys.stdin.readline().split()))

for num in cnt:
    if num in cards:
        print(cards[num], end = ' ')
    else:
        print(0, end = ' ')