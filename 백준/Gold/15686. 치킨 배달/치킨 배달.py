import sys
from collections import deque
from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def chicken(lst):

    check = lst
    q = deque(lst)
    dis = 0

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dr[k]
            ny = y + dc[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and (nx, ny) not in check:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
                if arr[nx][ny] == 1:
                    dis += visited[nx][ny]

    return dis

loc = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            loc.append((i, j))

com = list(combinations(loc, M))
ans = int(1e9)
for r in range(len(com)):
    visited = [[0] * N for _ in range(N)]
    ans = min(ans, chicken(com[r]))
print(ans)