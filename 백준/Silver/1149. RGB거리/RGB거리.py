N = int(input())
col = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]
dp[0] = col[0]

for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + col[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + col[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + col[i][2]

print(min(dp[-1]))