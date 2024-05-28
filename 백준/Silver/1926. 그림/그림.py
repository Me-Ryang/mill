import sys
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def pic(x, y):

    global cnt, max_v

    area = 1
    q = deque()
    q.append((x, y))
    visited[x][y] = cnt

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0 and arr[nr][nc] == 1:
                visited[nr][nc] = cnt
                area += 1
                q.append((nr, nc))

    max_v = max(max_v, area)
    return max_v

cnt, max_v = 0, 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            cnt += 1
            pic(i, j)

print(cnt)
print(max_v)