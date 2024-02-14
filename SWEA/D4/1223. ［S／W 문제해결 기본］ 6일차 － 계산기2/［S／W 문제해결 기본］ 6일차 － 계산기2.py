for t in range(10):
    N = int(input())
    string = input().split("+")
    p = {"*" : 3, "/" : 3, "+" : 1, "-" : 1}
    ans = 0
    
    for i in string:
        lst = []
        result = 1
        if '*' in i:
            lst = i.split('*')
            for j in lst:
                result *= int(j)
            ans += result
        else:
            ans += int(i)
    print(f"#{t+1}", ans)
