import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
table = list(input())

hamburger = deque()
person = deque()
count = 0

for i in range(N):
    if table[i] == 'H':
        hamburger.append(i)
    else:
        person.append(i)

while person and hamburger:
    p = person.popleft()
    h = hamburger.popleft()

    if abs(p - h) <= K:
        count += 1

    else:
        if p < h:
            hamburger.appendleft(h)
        else:
            person.appendleft(p)

print(count)