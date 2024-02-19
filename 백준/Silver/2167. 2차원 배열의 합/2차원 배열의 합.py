N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
for k in range(K):
    i, j, x, y = map(int, input().split())
    SUM = 0
    for r in range(i - 1, x): # 0
        for c in range(j - 1, y): # 1
            SUM += arr[r][c]
    print(SUM)