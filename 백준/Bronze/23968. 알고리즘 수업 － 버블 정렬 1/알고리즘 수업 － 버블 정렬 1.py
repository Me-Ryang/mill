N, K = list(map(int, input().split()))

A = list(map(int, input().split()))

count = 0
for i in range(len(A) - 1, 0, -1):
    for j in range(0, i):
        if A[j] > A[j + 1]:
            count += 1
            A[j], A[j + 1] = A[j + 1], A[j]
            if count == K:
                print(A[j], A[j + 1])
if count < K:
    print(-1)