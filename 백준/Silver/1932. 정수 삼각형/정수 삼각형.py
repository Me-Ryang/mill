import sys

n = int(input())
tri = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0] * (i + 1) for i in range(n)]
dp[0][0] = tri[0][0]

for i in range(1, n):
    for j in range(i + 1):
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + tri[i][j])
        if j < i:
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + tri[i][j])

print(max(dp[n - 1]))