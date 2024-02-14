for t in range(10):
    N = int(input())
    string = input()
    ex = {'*' : 2, '+' : 1, '(' : 3, ')' : 3} # 외부
    en = {'*' : 2, '+' : 1, '(' : 0, ')' : 3} # 내부

    def change(string):

        stack = []
        ans = ""
        for i in string:
            if i in ex:
                if i in "(+*":
                    while stack and ex[i] <= en[stack[-1]]:
                        ans += stack.pop()
                    stack.append(i)

                else:
                    while stack and stack[-1] != '(':
                        ans += stack.pop()
                    stack.pop()
            else:
                ans += i
        while stack:
            ans += stack.pop()
        
        return ans


    def calculate(ch):

        lst = []
        for i in ch:
            if i not in "+*":
                lst.append(int(i))
            else:
                if i == '*':
                    a = lst.pop()
                    b = lst.pop()
                    lst.append(a*b)
                else:
                    a = lst.pop()
                    b = lst.pop()
                    lst.append(a+b)

        return lst.pop()

    ch = change(string)
    ans = calculate(ch)
    print(f"#{t+1}", ans)
    