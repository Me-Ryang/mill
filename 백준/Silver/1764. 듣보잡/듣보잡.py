N, M = map(int, input().split())
listen = set(input() for _ in range(N))

cnt = 0
ans = []
for _ in range(M):
    name = input()
    if name in listen:
        cnt += 1
        listen.remove(name)
        ans.append(name)

print(cnt)
ans.sort()
for idx in range(cnt):
    print(ans[idx])