import sys

C = int(input())

def pick(n):
    global max_val

    if n == 11:
        max_val = max(max_val, sum(lst))
        return

    for i in range(11):
        if visited[i] or not arr[n][i]:
            continue
        visited[i] = 1
        lst.append(arr[n][i])
        pick(n + 1)
        lst.pop()
        visited[i] = 0

for _ in range(C):
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(11)]
    visited = [0] * 11

    max_val = 0
    lst = []

    pick(0)
    print(max_val)