def calculate(lst):

    stack = []
    ans = 0
    for i in lst:
        if not stack:
            stack.append(int(i))
            ans= int(i)
        elif i != '+':
            ans = int(i) + stack[-1]
            stack.append(ans)
        
    return ans


for t in range(10):
    N = int(input())
    string = input()
    result = calculate(string)

    print(f"#{t+1}", result)