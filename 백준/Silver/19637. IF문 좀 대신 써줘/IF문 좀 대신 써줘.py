import sys

N, M = map(int, input().split())

level = []
for _ in range(N):
    l, v = sys.stdin.readline().split()
    level.append((l, int(v)))

for _ in range(M):
    fight = int(sys.stdin.readline())
    left = 0
    right = N - 1
    while left <= right:
        mid = (left + right) // 2
        if fight > level[mid][1]:
            left = mid + 1
        else:
            right = mid - 1
    print(level[left][0])