import sys

N = int(input())
seq = list(map(int, sys.stdin.readline().split()))
stack = [0]
ans = [-1] * N

for i in range(1, N):
    while stack and seq[stack[-1]] < seq[i]:
        ans[stack.pop()] = seq[i]
    stack.append(i)

print(*ans)