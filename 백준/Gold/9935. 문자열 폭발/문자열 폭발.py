string = input()
burst = input()
k = len(burst)

result = []

for s in string:
    result.append(s)
    if ''.join(result[-k:]) == burst:
        for _ in range(k):
            result.pop()

if len(result) != 0:
    print(''.join(result))
else:
    print('FRULA')