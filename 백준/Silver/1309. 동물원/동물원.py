N = int(input())

dp = [0] * N
dp[0] = 3

if N >= 2:
    dp[1] = 7
    for i in range(2, N):
        dp[i] = (2 * dp[i - 1] + dp[i - 2]) % 9901

print(dp[N - 1])