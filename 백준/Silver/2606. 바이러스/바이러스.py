n = int(input())
m = int(input())
cnt = 0

def dfs(start):
    
    global cnt
    visited[start] = 1
    
    for w in arr[start]:
        if visited[w] == 0:
            cnt += 1
            dfs(w)
    return cnt
              
visited = [0] * (n + 1)
arr = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u) # 무방향

print(dfs(1))