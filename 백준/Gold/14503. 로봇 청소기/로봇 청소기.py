from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
cnt = 0

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(i, j, d):
    global cnt
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    cnt += 1

    while q:
        x, y = q.popleft()
        flag = 0

        for _ in range(4):
            d = (d + 3) % 4
            nx = x + dr[d]
            ny = y + dc[d]

            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1
                flag = 1
                break

        if flag == 0:
            if arr[x - dr[d]][y - dc[d]] != 1:
                q.append((x - dr[d], y - dc[d]))
            else:
                print(cnt)
                break

bfs(r, c, d)