import sys
input = sys.stdin.readline

def find_parent(parent, x):

    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):

    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = [0] * (N + 1)

for i in range(1, N + 1):
    parent[i] = i

routes = []
for _ in range(M):
    a, b, cost = map(int, input().split())
    routes.append((cost, a, b))

routes.sort()
result = 0
max_val = 0

for route in routes:
    cost, a, b = route
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        max_val = cost

print(result - max_val)