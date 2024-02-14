T = int(input())
for t in range(T):
    N = int(input())
    price = list(map(int, input().split()))

    ans = 0
    sell = price.pop()
    for i in range(len(price)):
        if not price:
            break

        if price[-1] <= sell:
            ans += sell - price.pop()

        elif price[-1] >= sell:
            sell = price.pop()
    
    print(f"#{t+1}", ans)