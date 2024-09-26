def solution(numbers):
    
    str_num = list(map(str, numbers))
    str_num.sort(key=lambda x: (x*4)[:4], reverse = True)
        
    return str(int(''.join(str_num)))
