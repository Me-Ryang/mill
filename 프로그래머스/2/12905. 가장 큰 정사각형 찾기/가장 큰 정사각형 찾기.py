# 16:14 ~

def solution(board):

    n = len(board)
    m = len(board[0])
    dp = [[0] * m for _ in range(n)]
    max_side = 0 # 가장 큰 정사각형의 한 변 길이
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                if i == 0 or j == 0: # 첫 번째 행이나 열은 그대로 복사
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_side = max(max_side, dp[i][j])

    return max_side ** 2