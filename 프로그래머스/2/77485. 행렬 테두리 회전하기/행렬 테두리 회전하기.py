# 17:20 ~

# 회전하는 숫자들 중 가장 작은 값 반환
def find_min(matrix, x1, y1, x2, y2):
    
    # 회전 시작 위치 값 저장
    prev_value = matrix[x1][y1]
    min_value = prev_value
    
    for c in range(y1 + 1, y2 + 1): # 상단 행 이동
        matrix[x1][c], prev_value = prev_value, matrix[x1][c]
        min_value = min(min_value, prev_value)
    for r in range(x1 + 1, x2 + 1): # 오른쪽 열 이동
        matrix[r][y2], prev_value = prev_value, matrix[r][y2]
        min_value = min(min_value, prev_value)
    for c in range(y2 - 1, y1 - 1, -1): # 하단 행 이동
        matrix[x2][c], prev_value = prev_value, matrix[x2][c]
        min_value = min(min_value, prev_value)
    for r in range(x2 - 1, x1 - 1, -1): # 왼쪽 열 이동
        matrix[r][y1], prev_value = prev_value, matrix[r][y1]
        min_value = min(min_value, prev_value)

    return min_value

def solution(rows, columns, queries):
    
    # 최초 행렬 만들기
    matrix = [[j for j in range(columns * i + 1, columns * (i + 1) + 1)] for i in range(rows)]
    
    answer = []
    for q in queries:
        x1, y1, x2, y2 = q
        val = find_min(matrix, x1 - 1, y1 - 1, x2 - 1, y2 - 1)
        answer.append(val)

    return answer