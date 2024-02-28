N = int(input())
path = list(map(int, input().split()))

ans = []
while path:
    up = []
    n1 = path.pop()
    up.append(n1)
    
    for _ in range(len(path)):
        n2 = path.pop()
        if n2 < n1:
            up.append(n2)
            n1 = n2
        else: # num < n
            path.append(n2)
            break

    ans.append(max(up) - min(up))

print(max(ans))   