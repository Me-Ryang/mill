import sys
sys.setrecursionlimit(10 ** 6)
N, M, R = map(int, input().split())
loc = [map(int,sys.stdin.readline().split()) for _ in range(M)]

adjl = [[] for _ in range(N + 1)]
visited = [-1] * (N + 1)


def dfs(i, dep):  # 시작 i, 깊이 dep
    visited[i] = dep

    for w in adjl[i]:
        if visited[w] == -1:
            dfs(w, dep + 1)
    return

for u, v in loc:
    adjl[u].append(v)
    adjl[v].append(u)  # 무방향

for s in adjl:
    s.sort(reverse=True)

dfs(R, 0)
for n in range(1, N + 1):
    print(visited[n])