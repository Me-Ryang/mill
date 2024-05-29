N, M = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0] * N
arr.sort()
seq = []

def nnm():

    if len(seq) == M:
        print(*seq)
        return

    before = 0
    for i in range(N):
        if visited[i] == 0 and before != arr[i]:
            visited[i] = 1
            before = arr[i]
            seq.append(arr[i])
            nnm()
            seq.pop()
            visited[i] = 0

nnm()