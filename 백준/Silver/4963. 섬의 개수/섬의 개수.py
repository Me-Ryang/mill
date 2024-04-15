import sys
sys.setrecursionlimit(10**6)

def island_count(i, j):

    global cnt

    visited[i][j] = cnt

    for k in range(8):
        ni = i + dr[k]
        nj = j + dc[k]
        if 0 <= ni < h and 0 <= nj < w and visited[ni][nj] == 0 and island[ni][nj] == 1:
            visited[ni][nj] = cnt
            island[ni][nj] = 0
            island_count(ni, nj)

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    island = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                cnt += 1
                island_count(i, j)

    print(cnt)