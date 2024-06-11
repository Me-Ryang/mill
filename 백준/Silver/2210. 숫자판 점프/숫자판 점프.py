import sys
sys.setrecursionlimit(10 ** 6)

N = 5
arr = [list(input().split()) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

ans = []

def set(n, x, y):

    if n == 6:
        new = int(''.join(nums))
        if new not in ans:
            ans.append(new)
            return

    if n > 6:
        return

    for k in range(4):
        nx = x + dr[k]
        ny = y + dc[k]
        if 0 <= nx < N and 0 <= ny < N:
            nums.append(arr[nx][ny])
            set(n + 1, nx, ny)
            nums.pop()

for i in range(N):
    for j in range(N):
        nums = []
        nums.append(arr[i][j])
        set(1, i, j)

print(len(ans))