import sys
from collections import deque

N, K = map(int, input().split())
virus = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

q = []
for i in range(N):
    for j in range(N):
        if virus[i][j] != 0:
            q.append((i, j, virus[i][j], 0))

q.sort(key=lambda x : x[2])
q = deque(q)

while q:

    r, c, val, s = q.popleft()

    if s == S:
        break

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N and virus[nr][nc] == 0:
            virus[nr][nc] = val
            q.append((nr, nc, val, s + 1))

print(virus[X - 1][Y - 1])