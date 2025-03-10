N = int(input())
i = 1
start = 1

while True:

    if start >= N:
        break
    start += 6 * i
    i += 1

print(i)