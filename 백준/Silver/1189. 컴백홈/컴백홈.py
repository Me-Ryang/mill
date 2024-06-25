import sys
sys.setrecursionlimit(10 ** 6)

R, C, K = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
cnt = 0

def home(start_x, start_y):

    global cnt

    if visited[start_x][start_y] > K:
        return

    for k in range(4):
        nx = start_x + dr[k]
        ny = start_y + dc[k]
        if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] != 'T' and visited[nx][ny] == 0:
            visited[nx][ny] = visited[start_x][start_y] + 1
            if nx == 0 and ny == C - 1 and visited[nx][ny] == K:
                cnt += 1
            home(nx, ny)
            visited[nx][ny] = 0

visited[R - 1][0] = 1
home(R - 1, 0)
print(cnt)