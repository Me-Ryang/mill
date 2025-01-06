N, K = map(int, input().split())
coin = []
cnt = 0

for _ in range(N):
    val = int(input())
    coin.append(val)

coin_rev = sorted(coin, reverse=True)

for money in coin_rev:
    count = K // money
    if K == 0:
        break

    if count == 0:
        continue

    cnt += count
    K %= money

print(cnt)