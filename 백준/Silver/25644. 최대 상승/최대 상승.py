N = int(input())
stock = list(map(int, input().split()))

benefit, result = 0, 0
for i in range(N - 1, -1, -1):
    benefit = max(benefit, stock[i])
    result = max(result, benefit - stock[i])

print(result)