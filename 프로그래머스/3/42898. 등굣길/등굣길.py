def solution(m, n, puddles):
    visited = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                visited[i][j] = 1
            elif [j, i] in puddles:
                visited[i][j] = 0
            else:
                visited[i][j] = (visited[i - 1][j] + visited[i][j - 1]) % 1000000007
    
    return visited[n][m]