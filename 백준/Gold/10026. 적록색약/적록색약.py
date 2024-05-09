import copy
from collections import deque

N = int(input())
arr = [list(input()) for _ in range(N)]
arr_2 = copy.deepcopy(arr)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def normal(x, y, col):

    global cnt

    arr[x][y] = 0
    q = deque()
    q.append((x, y))

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == col:
                arr[nr][nc] = 0
                q.append((nr, nc))

def red_green(x, y, col):

    global count

    flag = 0
    arr_2[x][y] = 0
    q = deque()
    q.append((x, y))

    if col != 'B':
        flag = 1

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and arr_2[nr][nc] != 0:
                if flag == 0 and arr_2[nr][nc] == col:
                    arr_2[nr][nc] = 0
                    q.append((nr, nc))
                elif flag == 1 and arr_2[nr][nc] != 'B':
                    arr_2[nr][nc] = 0
                    q.append((nr, nc))

cnt, count = 0, 0
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            cnt += 1
            normal(i, j, arr[i][j])

for i in range(N):
    for j in range(N):
        if arr_2[i][j] != 0:
            count += 1
            red_green(i, j, arr_2[i][j])

print(cnt, count)