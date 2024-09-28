from itertools import permutations

def solution(k, dungeons):
     
    global answer
    answer = 0
        
    for perm in permutations(dungeons):
        current_k = k
        count = 0
        
        for dungeon in perm:
            need, minus = dungeon
            if current_k >= need:
                current_k -= minus
                count += 1
            else:
                break
        
        answer = max(answer, count)
    
    return answer