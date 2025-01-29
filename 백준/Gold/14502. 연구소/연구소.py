import sys
from itertools import combinations
from collections import deque
from copy import deepcopy

N, M = map(int, sys.stdin.readline().split())
map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
safe, virus = [], []

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for i in range(N):
    for j in range(M):
        if map[i][j] == 0:
            safe.append((i, j))
        elif map[i][j] == 2:
            virus.append((i, j))

def virus_full(new_map):

    virus_q = deque(virus)

    while virus_q:
        r, c = virus_q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and new_map[nr][nc] == 0:
                new_map[nr][nc] = 2
                virus_q.append((nr, nc))

answer = 0
for wall in list(combinations(safe, 3)):
    q = deque(wall)
    new_map = deepcopy(map)
    while q:
        r, c = q.popleft()
        new_map[r][c] = 1

    virus_full(new_map)
    result = 0
    for i in range(N):
        result += new_map[i].count(0)

    answer = max(answer, result)

print(answer)