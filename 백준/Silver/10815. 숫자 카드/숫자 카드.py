import sys

N = int(input())
num = set(map(int, sys.stdin.readline().split()))
M = int(input())
number = list(map(int, sys.stdin.readline().split()))

for n in number:
    if n in num:
        print(1, end = ' ')
    else:
        print(0, end = ' ')