T = int(input())

for _ in range(T):

    VPS = list(input())
    stack = []

    for str in VPS:
        if str == '(':
            stack.append(str)
        elif '(' in stack and str == ')':
            stack.pop()
        else:
            stack.append(str)

    if stack:
        print('NO')
    else:
        print('YES')