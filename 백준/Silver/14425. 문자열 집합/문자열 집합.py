N, M = map(int, input().split())

S = set(input() for _ in range(N))

cnt = 0
for _ in range(M):
    check = input()
    if check in S:
        cnt += 1

print(cnt)
