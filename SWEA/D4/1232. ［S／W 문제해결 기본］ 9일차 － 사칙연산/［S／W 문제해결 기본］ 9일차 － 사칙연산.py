def postorder(start):
    global result

    if start:
        postorder(left[start])
        postorder(right[start])
        ans.append(tree[start])
        if str(tree[start]) not in '+-/*':
            result.append(tree[start])
        else:
            if tree[start] == '*':
                a = result.pop()
                b = result.pop()
                result.append(a*b)
            elif tree[start] == '+':
                a = result.pop()
                b = result.pop()
                result.append(a+b)
            elif tree[start] == '-':
                a = result.pop()
                b = result.pop()
                if a > b:
                    result.append(a-b)
                else:
                    result.append(b-a)
            elif tree[start] == '/':
                a = result.pop()
                b = result.pop()
                if a > b:
                    result.append(a/b)
                else:
                    result.append(b/a)



for t in range(10):
    N = int(input())
    tree = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    ans = []
    for i in range(N):
        node, value, *a = map(str, input().split())
        if len(a) == 2:
            l, r = a
            tree[int(node)] = value
            left[int(node)] = int(l)
            right[int(node)] = int(r)
        else:
            if value in "-+/*":
                tree[int(node)] = value
            else:
                tree[int(node)] = int(value)    
    result = []
    postorder(1)
    print(f"#{t+1}", int(result[0]))
