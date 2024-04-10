import sys
sys.setrecursionlimit(10**6)

N, M, K = map(int, sys.stdin.readline().split())
arr = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]

for k in range(K):
    i, j = map(int, sys.stdin.readline().split())
    arr[i - 1][j - 1] = 1

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def food(r, c):

    global cnt

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1 and visited[nr][nc] == 0:
            cnt += 1
            visited[nr][nc] = cnt
            food(nr, nc)

for r in range(N):
    for c in range(M):
        if arr[r][c] == 1 and visited[r][c] == 0:
            cnt = 1
            visited[r][c] = 1
            food(r, c)

MAX = 0
for x in range(N):
    for y in range(M):
        if visited[x][y] > MAX:
            MAX = visited[x][y]

print(MAX)