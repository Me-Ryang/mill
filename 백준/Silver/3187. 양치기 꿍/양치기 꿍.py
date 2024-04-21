from collections import deque

R, C = map(int, input().split())
Gung = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

sheep = 0
wolf = 0

def hunt(x, y):

    global sheep, wolf, s, w

    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < R and 0 <= nc < C and visited[nr][nc] == 0 and Gung[nr][nc] != '#':
                if Gung[nr][nc] == 'k':
                    s += 1
                elif Gung[nr][nc] == 'v':
                    w += 1
                visited[nr][nc] = 1
                q.append((nr, nc))
                Gung[nr][nc] = '#'

    if s > w:
        w = 0
    else:
        s = 0

    sheep += s
    wolf += w

for i in range(R):
    for j in range(C):
        s, w = 0, 0
        if Gung[i][j] == 'k':
            s = 1
            hunt(i, j)
        elif Gung[i][j] == 'v':
            w = 1
            hunt(i, j)

print(sheep, wolf)