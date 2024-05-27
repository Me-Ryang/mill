from collections import deque

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def border(start_x, start_y):

    q = deque()
    q.append((start_x, start_y))
    union = [(start_x, start_y)]
    people = arr[start_x][start_y]
    cnt = 1

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dr[d]
            ny = y + dc[d]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if abs(arr[x][y] - arr[nx][ny]) >= L and abs(arr[x][y] - arr[nx][ny]) <= R:
                    visited[nx][ny] = 1
                    people += arr[nx][ny]
                    cnt += 1
                    q.append((nx, ny))
                    union.append((nx, ny))

    for i, j in union:
        arr[i][j] = people // cnt

    return cnt > 1

n = 0
while True:
    isMoved = False
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                if border(i, j):
                    isMoved = True
    if not isMoved:
        break
    n += 1

print(n)