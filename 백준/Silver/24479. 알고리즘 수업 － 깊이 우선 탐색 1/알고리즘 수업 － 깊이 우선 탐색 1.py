import sys
sys.setrecursionlimit(10 ** 6)

N, M, R = map(int, sys.stdin.readline().split())
adjl = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adjl[u].append(v)
    adjl[v].append(u)

def dfs(start):
    global cnt
    visited[start] = cnt
    adjl[start].sort()
    for i in adjl[start]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

cnt = 1
dfs(R)
for n in range(1, N + 1):
    print(visited[n])