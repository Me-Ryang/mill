N, M = map(int, input().split())
cards = list(map(int, input().split()))
n = len(cards)

MAX = 0
for one in range(n):
    for two in range(one + 1, n):
        for three in range(two + 1, n):
            black = cards[one] + cards[two] + cards[three]
            if black <= M:
                if MAX < black:
                    MAX = black
print(MAX)