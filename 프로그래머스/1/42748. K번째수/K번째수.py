def solution(array, commands):
    answer = []
    for cut in commands:
        i, j, k = cut[0], cut[1], cut[2]
        n_array = array[i-1:j]
        n_array.sort()
        answer.append(n_array[k-1])
    return answer