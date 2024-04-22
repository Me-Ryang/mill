import sys

N, Q = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
A.sort()

dp = [0] * (N + 1)
dp[1] = A[0]
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + A[i - 1]

for r in range(Q):
    L, R = map(int, sys.stdin.readline().split())
    print(dp[R] - dp[L - 1])