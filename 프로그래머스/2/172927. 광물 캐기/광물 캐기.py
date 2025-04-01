def solution(picks, minerals):

    # 곡괭이의 수
    num = sum(picks)
    # 곡괭이로 캘 수 있는 광물의 수    
    minerals = minerals[:num*5]
    n = len(minerals)
    
    minerals_cnt = []
    for i in range(0, n, 5):
        dia = minerals[i:i+5].count('diamond')
        iron = minerals[i:i+5].count('iron')
        stone = minerals[i:i+5].count('stone')
        minerals_cnt.append([dia, iron, stone])
    
    minerals_cnt.sort(key=lambda x: (-x[0], -x[1], -x[2]))
    
    fati = 0
    for minerals in minerals_cnt:
        if picks[0] > 0:
            picks[0] -= 1
            fati += sum(minerals)
        elif picks[1] > 0:
            picks[1] -= 1
            fati += 5 * minerals[0] + minerals[1] + minerals[2]
        elif picks[2] > 0:
            picks[2] -= 1
            fati += 25 * minerals[0] + 5 * minerals[1] + minerals[2]
  
    return fati