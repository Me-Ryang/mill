import sys

H, W, X, Y = map(int, input().split())
A = [[0] * W for _ in range(H)]
B = [list(map(int, sys.stdin.readline().split())) for _ in range(H + X)]

for i in range(H + X):
    for j in range(W + Y):
        if i >= H or j >= W:
            break
        if i >= X and j >= Y:
            A[i][j] = B[i][j] - B[i - X][j - Y]
            B[i][j] = A[i][j]
        else:
            A[i][j] = B[i][j]

for r in range(H):
    print(*A[r])