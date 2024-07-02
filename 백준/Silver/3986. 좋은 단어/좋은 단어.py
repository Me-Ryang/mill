N = int(input())
cnt = 0
for _ in range(N):
    word = list(input())
    stack = []

    if len(word) % 2 == 1:
        continue

    while word:
        x = word.pop()
        if not stack:
            stack.append(x)
        else:
            if stack[-1] == x:
                stack.pop()
            else:
                stack.append(x)

    if not stack:
        cnt += 1

print(cnt)