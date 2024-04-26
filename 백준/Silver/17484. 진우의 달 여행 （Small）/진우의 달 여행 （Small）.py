import sys

N, M = map(int, sys.stdin.readline().split())
moon = [list(map(int, input().split())) for _ in range(N)]

dir = [-1, 0, 1]

def universe(r, c, before, low, answer):
    if r == N - 1:
        return min(low, answer)

    for k in range(3):
        if dir[k] != before:
            if 0 <= r < N and 0 <= c + dir[k] < M:
                low = universe(r + 1, c + dir[k], dir[k], low, answer + moon[r + 1][c + dir[k]])
    return low

low = int(1e9)
for i in range(M):
    low = min(universe(0, i, 2, low, moon[0][i]), low)

print(low)