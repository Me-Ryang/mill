H, W, N, M = map(int, input().split())

w_cnt = 0
for i in range(0, W, M + 1):
    if i < W:
        w_cnt += 1

h_cnt = 0
for i in range(0, H, N + 1):
    if i < H:
        h_cnt += 1

print(w_cnt * h_cnt)