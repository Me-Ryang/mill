def nnm():
    if len(lst) == M:
        print(*lst)
        return

    for n in range(1, N+1):
        if n not in lst:
            lst.append(n)
            nnm()
            lst.pop()

N, M = map(int, input().split())
lst = []

nnm()