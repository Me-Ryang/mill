N = int(input())
postfix = list(input())
var = 0

# 연산자 할당

numbers = []
for _ in range(N):
    num = int(input())
    numbers.append(num) # numbers.append(int(input()))

stack = []
for tk in postfix:
    if tk not in '+-*/': # 피연산자
        stack.append(numbers[ord(tk) - ord('A')])
    # 후위표기식 계산
    else:
        n1 = stack.pop()
        n2 = stack.pop()
        if tk == '+':
            stack.append(n2 + n1)
        elif tk == '-':
            stack.append(n2 - n1)
        elif tk == '*':
            stack.append(n2 * n1)
        else: # tk == '/'
            stack.append(n2 / n1)    

print(format(stack[0], ".2f"))