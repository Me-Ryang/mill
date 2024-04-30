from collections import deque

N, M = map(int, input().split())
war = [list(input()) for _ in range(M)]
visited = [[0] * N for _ in range(M)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def strong(x, y, color):

    global cnt

    war[x][y] = 0
    visited[x][y] = 1
    q = deque()
    q.append((x, y))

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < M and 0 <= nc < N and visited[nr][nc] == 0 and war[nr][nc] == color:
                visited[nr][nc] = 1
                war[nr][nc] = 0
                cnt += 1
                q.append((nr, nc))

strong_w = 0
strong_b = 0

for i in range(M):
    for j in range(N):
        cnt = 1
        if war[i][j] == 'W':
            strong(i, j, war[i][j])
            strong_w += cnt ** 2
        elif war[i][j] == 'B':
            strong(i, j, war[i][j])
            strong_b += cnt ** 2

print(strong_w, strong_b)