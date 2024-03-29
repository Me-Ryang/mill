N, K = map(int, input().split())
medal = [list(map(int, input().split())) for _ in range(N)]
medal.sort(key = lambda x:(-x[1], -x[2], -x[3]))

for i in range(N):
    if medal[i][0] == K:
        idx = i

for rank in range(1, N + 1):
    if medal[idx][1:] == medal[rank - 1][1:]:
        print(rank)
        break