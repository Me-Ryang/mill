K = int(input())

dp = [[0, 0] for _ in range(K + 1)]
dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, K + 1):
    dp[i][0] = dp[i - 1][1]
    dp[i][1] = dp[i - 1][0] + dp[i - 1][1]

print(*dp[K])