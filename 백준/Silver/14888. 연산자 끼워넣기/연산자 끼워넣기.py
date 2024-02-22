import sys
from collections import deque

p = {"*" : 1, "/" : 1, "+" : 1, "-" : 1}

def change(string):

    lst = []
    word = ""
    for i in string:
        if i not in "+*/-":
            word += i
        else:
            lst.append(int(word))
            lst.append(i)
            word =""
    lst.append(int(word))

    return lst


def dfs(string, lv):

    if len(string) == n + len(cal_lst)-1:
        result.append(string)
        return

    for i in range(1, len(lst)):
        if visited[i] == 0:
            visited[i] = 1
            stack.append(string + str(cal_lst[i]))
            dfs(string + str(cal_lst[i])+str(lst[lv-1]), lv+1)
            stack.pop()
            visited[i] = 0


def calculate(lst):

    queue = deque()
    for i in range(len(lst)):
        if i%2 == 0:
            queue.append(lst[i])
    
    for j in range(len(lst)):
        if j % 2 != 0:
            if lst[j] == "+":
                a = queue.popleft()
                b = queue.popleft()
                queue.appendleft(a+b)
            elif lst[j] == "-":
                a = queue.popleft()
                b = queue.popleft()
                queue.appendleft(a-b)
            elif lst[j] == "*":
                a = queue.popleft()
                b = queue.popleft()
                queue.appendleft(a*b)
            elif lst[j] == "/":
                a = queue.popleft()
                b = queue.popleft()
                queue.appendleft(int(a/b))
    return queue.popleft()

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst1 = list(map(str, lst))
n = 0
for i in lst1:
    n += len(i)

cal = ['+', '-', '*', '/']
c = list(map(int, sys.stdin.readline().split()))
cal_lst = [0]
for i in range(len(c)):
    for j in range(c[i]):
        cal_lst.append(cal[i])

stack = [str(lst[0])]
visited = [0] * (N+len(cal_lst))
result = []
dfs(str(lst[0]), 2)
max_num = -1e10
min_num = 1e10
for i in result:
    ans = change(i)
    num = calculate(ans)
    if max_num < num:
        max_num = num
    if min_num > num:
        min_num = num

print(int(max_num))
print(int(min_num))