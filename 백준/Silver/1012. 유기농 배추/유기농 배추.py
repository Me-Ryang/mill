from collections import deque

T = int(input())

def organic(x, y):
    global cnt

    q = deque()
    q.append((x, y))
    visited[x][y] = cnt

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < M and 0 <= nc < N and visited[nr][nc] == 0 and cabbage[nr][nc] == 1:
                visited[nr][nc] = cnt
                cabbage[nr][nc] = 0
                q.append((nr, nc))

for _ in range(T):
    M, N, K = map(int, input().split())
    cabbage = [[0] * N for _ in range(M)]
    visited = [[0] * N for _ in range(M)]

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    for _ in range(K):
        X, Y = map(int, input().split())
        cabbage[X][Y] = 1

    cnt = 0
    for i in range(M):
        for j in range(N):
            if cabbage[i][j] == 1:
                cnt += 1
                organic(i, j)

    print(cnt)