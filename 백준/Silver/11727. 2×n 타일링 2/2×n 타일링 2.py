n = int(input())

rec = [0] * 1001

rec[1] = 1
rec[2] = 3

for num in range(3, n + 1):
    rec[num] = 2 * rec[num - 2] + rec[num - 1]

print(rec[n] % 10007)