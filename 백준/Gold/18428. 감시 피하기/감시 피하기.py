from itertools import combinations
from copy import deepcopy

N = int(input())
ts = [list(input().split()) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

x, t = [], []
for i in range(N):
    for j in range(N):
        if ts[i][j] == 'X':
            x.append((i, j))
        elif ts[i][j] == 'T':
            t.append((i, j))

def avoid(new_ts):

    for r, c in t:
        for k in range(4):
            nr, nc = r, c
            while True:
                nr += dr[k]
                nc += dc[k]
                if 0 > nr or nr >= N or 0 > nc or nc >= N:
                    break
                if new_ts[nr][nc] == 'S':
                    return False
                elif new_ts[nr][nc] == 'O':
                    break

    return True

answer = 'NO'
for loc in list(combinations(x, 3)):
    new_ts = deepcopy(ts)

    for r, c in loc:
        new_ts[r][c] = 'O'

    if avoid(new_ts):
        answer = 'YES'
        break
    else:
        continue

print(answer)