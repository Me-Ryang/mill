N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N

def team(x, n):

    global min_v

    if x == N // 2:
        start, link = 0, 0
        for r in range(N):
            for c in range(N):
                if visited[r] and visited[c]:
                    start += arr[r][c]
                elif not visited[r] and not visited[c]:
                    link += arr[r][c]
        min_v = min(min_v, abs(start-link))
        return

    for i in range(n, N):
        if visited[i] == 0:
            visited[i] = 1
            team(x + 1, i + 1)
            visited[i] = 0

min_v = int(1e9)
team(0, 0)

print(min_v)