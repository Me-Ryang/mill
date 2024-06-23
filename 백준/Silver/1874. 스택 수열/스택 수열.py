n = int(input())
final = [int(input()) for _ in range(n)]

stack = []
result = []
cal = []
loc = 0
num = 1

while loc < n:
    while num <= final[loc]:
        stack.append(num)
        cal.append('+')
        num += 1

    if stack[-1] == final[loc]:
        stack.pop()
        cal.append('-')
        loc += 1
    else:
        print('NO')
        break
else:
    for x in cal:
        print(x)