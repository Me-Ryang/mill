from collections import deque
from itertools import combinations
from copy import deepcopy

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
answer = 999999999

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

chicken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append((i, j))

comb_chicken = list(combinations(chicken, M))

for drive in comb_chicken:
    loc = deque(drive)
    new_city = deepcopy(city)
    visited = [[0] * N for _ in range(N)]
    for i in range(M):
        new_city[loc[i][0]][loc[i][1]] = 3
    result = 0
    while loc:
        start = loc.popleft()
        r, c = start[0], start[1]
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and new_city[nr][nc] != 3 and visited[nr][nc] == 0:
                if city[nr][nc] == 1:
                    result += visited[r][c] + 1
                    new_city[nr][nc] = 0
                visited[nr][nc] = visited[r][c] + 1
                loc.append((nr, nc))
    answer = min(answer, result)

print(answer)
