def solution(s):
    s_list = list(map(int, s.split()))
    answer = str(min(s_list))
    answer += ' '
    answer += str(max(s_list))
    return answer