# 현재 설치된 구조물이 가능한 구조물인지 확인하는 함수
def possible(answer):
    
    for x, y, a in answer:
        if a == 0: # 설치된 것이 '기둥'인 경우
            # 바닥 위, 보의 한쪽 끝부분 위, 다른 기둥 위
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        elif a == 1: # 설치된 것이 '보'인 경우
            # 한쪽 끝 부분이 기둥 위, 양쪽 끝부분이 다른 보와 동시에 연결
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, a, b = frame
        if b == 0: # 삭제하는 경우
            answer.remove([x, y, a]) # 일단 삭제를 해본 뒤에
            if not possible(answer):
                answer.append([x, y, a])
        elif b == 1: # 설치하는 경우
            answer.append([x, y, a]) # 일단 설치를 해본 뒤에
            if not possible(answer):
                answer.remove([x, y, a])
    
    return sorted(answer)