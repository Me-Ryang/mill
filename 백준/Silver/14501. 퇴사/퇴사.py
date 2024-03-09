N = int(input())

work = []
for i in range(N):
    T, P = map(int, input().split())
    work.append([T, P])

benefit = [0] * (N + 1)
for r in range(N):
    for c in range(r + work[r][0], N + 1):
        if benefit[c] < benefit[r] + work[r][1]:
            benefit[c] = benefit[r] + work[r][1]

print(benefit[-1])