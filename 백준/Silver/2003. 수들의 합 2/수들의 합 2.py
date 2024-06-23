N, M = map(int, input().split())
A = list(map(int, input().split()))

s = A[0]
cnt = 0
l, r = 0, 1

while True:
    if s < M:
        if r < N:
            s += A[r]
            r += 1
        else:
            break
    elif s == M:
        cnt += 1
        s -= A[l]
        l += 1
    else:
        s -= A[l]
        l += 1

print(cnt)