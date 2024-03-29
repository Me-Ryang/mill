from collections import deque
N, K = map(int, input().split())
medal = [list(map(int, input().split())) for _ in range(N)]
medal.sort(key = lambda x:(-x[1], -x[2], -x[3]))
medal = deque(medal)
result = [0] * N

rank = 1
result[0] = 1
i, g, s, b = medal.popleft()
while medal:

    ni, ng, ns, nb = medal.popleft()
    if ng == g and ns == s and nb == b:
        result[ni - 1] = rank
        rank += 1
    else:
        rank += 1
        result[ni - 1] = rank
    g, s, b = ng, ns, nb

    if ni == K:
        break

print(result[K - 1])