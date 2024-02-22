dic = {"0001101" : 0, "0011001" : 1, "0010011" : 2, "0111101" : 3, "0100011" : 4,
       "0110001" : 5, "0101111" : 6, "0111011" : 7, "0110111" : 8, "0001011" : 9}

def check():

    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if mp[i][j] == '1':
                return i, j
               
    
def solution(end_x, end_y):
    
    lst = []
    result = []
    for k in range(end_y, end_y-56, -1):
        lst.append(mp[end_x][k])

    lst.reverse()
    for i in range(0, len(lst), 7):
        ans = ""
        for j in range(i, i+7):
            ans += lst[j]
        result.append(dic[ans])
    
    return result

def valid(pw_lst):

    odd = 0
    even = 0

    for i in range(len(pw_lst)):
        if i % 2 != 0:
            even += pw_lst[i]
        else:
            odd += pw_lst[i]
    
    if (odd*3 + even) % 10 == 0:
        return True
    else:
        return False


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    mp = [list(input()) for _ in range(N)]
    x, y = check()
    r = solution(x, y)
    h = valid(r)
    a = 0
    if h == True:
        for i in r:
            a += i
        print(f"#{t+1}", a)
    else:
        print(f"#{t+1}", 0)