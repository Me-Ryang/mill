import sys

N, X = map(int, sys.stdin.readline().split())
visit = list(map(int, sys.stdin.readline().split()))

dp = [0] * N
dp[0] = visit[0]

for i in range(1, N):
    if i < X:
        dp[i] = dp[i - 1] + visit[i]
    else:
        dp[i] = dp[i - 1] - visit[i - X] + visit[i]

if max(dp) == 0:
    print('SAD')
else:
    print(max(dp))
    print(dp.count(max(dp)))