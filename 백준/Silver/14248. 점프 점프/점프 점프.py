import sys
from collections import deque

n = int(input())
Ai = list(map(int, sys.stdin.readline().split()))
visited = [0] * (n + 1)
s = int(input())

def stone(start):

    q = deque([start])
    cnt = 1

    while q:
        x = q.popleft()
        for y in (x - Ai[x - 1], x + Ai[x - 1]):
            if 0 < y <= n and visited[y] == 0:
                visited[y] = 1
                cnt += 1
                q.append(y)

    print(cnt)

stone(s)