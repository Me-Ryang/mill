from collections import Counter

def solution(topping):
    
    top_cnt = Counter(topping)
    me = set(topping)
    sister = set()
    
    ans = 0
    for i in topping:
        top_cnt[i] -= 1
        sister.add(i)
        if top_cnt[i] == 0:
            me.remove(i)
        if len(me) == len(sister):
            ans += 1
            
    return ans