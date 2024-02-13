import itertools

N, M = map(int, input().split())
num = list(range(1, N + 1))

arr = itertools.permutations(num, M)

for tp in arr:
    for per in tp:
        print(per, end = ' ')
    print()