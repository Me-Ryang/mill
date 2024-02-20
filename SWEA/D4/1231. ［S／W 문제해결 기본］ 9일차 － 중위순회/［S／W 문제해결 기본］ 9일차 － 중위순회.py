def in_order(rt):
    
    if rt:
        in_order(left[rt])
        ans.append(rt)
        in_order(right[rt])


for t in range(10):
    N = int(input())
    string = [0] * (N+1)
    left = [0] * (N+1)  
    right = [0] * (N+1)
    parent = [0] * (N+1)
    lst = []
    for i in range(N):
        a, b = 0, 0
        idx, st, *ls = map(str, input().split())
        if len(ls) > 1:
            a, b = ls[0], ls[1]
        elif len(ls) == 1:
            a = ls[0]
        idx, a, b = int(idx), int(a), int(b)
        string[idx] = st
        left[idx] = a
        right[idx] = b
        parent[a] = idx
        parent[b] = idx
    
    for j in parent:
        if parent[j] == 0:
            root = j

    ans = []
    in_order(root)
    
    result = ""
    for k in ans:
        result += string[k]
    print(f"#{t+1}", result)