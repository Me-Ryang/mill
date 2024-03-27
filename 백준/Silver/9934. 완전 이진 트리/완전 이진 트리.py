K = int(input())
building = list(map(int, input().split()))
tree = [[] for _ in range(K)]

def tree_level(lst, i):
    mid = len(lst) // 2
    tree[i].append(lst[mid])
    if len(lst) == 1:
        return
    tree_level(lst[:mid], i + 1)
    tree_level(lst[mid+1:], i + 1)

tree_level(building, 0)
for r in range(K):
    print(*tree[r])