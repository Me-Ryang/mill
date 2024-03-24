from collections import deque

def move(goal_x, goal_y):

    q = deque()
    q.append((goal_x, goal_y))
    visited[goal_x][goal_y] = 0

    while q:

        x, y = q.popleft()

        for k in range(4):
            nx = x + dr[k]
            ny = y + dc[k]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            goal_x = i
            goal_y = j
            break

move(goal_x, goal_y)

for r in range(n):
    for c in range(m):
        if arr[r][c] == 0:
            visited[r][c] = 0

for p in range(n):
    print(*visited[p])