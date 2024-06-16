from collections import deque

M, N = map(int, input().split())
visited = [[0] * N for _ in range(M)]
q = deque()
q.append((0, 0))
visited[0][0] = 1

cnt = 0
all = 1
move = deque([(0, 1), (1, 0), (0, -1), (-1, 0)])

while all < M * N:
    r, c = move.popleft()
    move.append((r, c))
    while all < M * N:
        x, y = q.popleft()
        nx = x + r
        ny = y + c
        if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            all += 1
            q.append((nx, ny))
        else:
            cnt += 1
            q.append((x, y))
            break

print(cnt)