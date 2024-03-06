while True:
    try:
        N = int(input())
        for idx in range(N + 1):
            if idx == 0:
                ans = '-'
            else:
                ans = ans + ' ' * len(ans) + ans
        print(ans)
    except:
        break