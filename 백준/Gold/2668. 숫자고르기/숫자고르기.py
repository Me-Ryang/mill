N = int(input())
first = [i for i in range(1, N + 1)]
lst = [[] for _ in range(N + 1)]
result = []

for i in range(N):
    u, v = first[i], int(input())
    lst[u].append(v)

def choose(x):

    if visited[x] == 0:
        visited[x] = 1

        for n in lst[x]:
            first.add(x)
            second.add(n)

            if first == second:
                result.extend(list(first))
                return

            choose(n)

    visited[x] = 0

for x in range(1, N + 1):
    visited = [0] * (N + 1)
    first, second = set(), set()
    choose(x)

ans = list(set(result))
ans.sort()
print(len(ans))
for a in ans:
    print(a)