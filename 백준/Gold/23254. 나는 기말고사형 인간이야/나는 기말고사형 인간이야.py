import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

lst = []
for i in range(M):
    study_time = (100 - A[i]) // B[i]
    lst.append((B[i], study_time))
    lst.append((100 - A[i] - B[i] * study_time, 1))

lst.sort(reverse=True)
score = sum(A)
total_time = 24 * N
for plus, time in lst:
    score += plus * min(time, total_time)
    total_time -= min(time, total_time)

print(score)