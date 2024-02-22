import sys

def dfs(string):
    global result, ans

    if string == N:
        set_lst.add(tuple(result))
        return
    elif string not in N:
        return
    
    for i in range(len(N)):
        if visited[i] == 0:

            result.append(string + lst[i])
            visited[i] = 1
            dfs(string + lst[i])
            result.pop()
            visited[i] = 0
            
            result.append(lst[i] + string)
            visited[i] = 1
            dfs(lst[i] + string)
            result.pop()
            visited[i] = 0


N = sys.stdin.readline().strip()
set_lst = set()
lst = list(N)
result = []

for i in range(len(lst)):
    visited = [0] * (len(N)+1)
    visited[i] = 1
    result.append(lst[i])
    dfs(lst[i])
    result.pop()
print(len(set_lst))