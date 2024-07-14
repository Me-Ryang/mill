import sys
N, M, K = map(int, input().split())
ans = 0
for _ in range(N):
    cnt = 0
    seat = sys.stdin.readline()
    for s in seat:
        if s == "0":
            cnt += 1
            if cnt == K:
                cnt -= 1
                ans += 1
        elif s == "1":
            cnt = 0

print(ans)