N, K = map(int, input().split())
temp = list(map(int, input().split()))

dp = [0] * (N - K + 1)
dp[0] = sum(temp[:K])

for i in range(1, N - K + 1):
    dp[i] = dp[i - 1] - temp[i - 1] + temp[i + K - 1]

print(max(dp))