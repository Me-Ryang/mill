import sys
A, B = map(int, sys.stdin.readline().split())

def cal(A, B):
    cnt = 0
    while True:
        try:
            if B % 2 == 0:
                n = B // 2
                B = B // 2
                cnt += 1
            elif int(str(B)[-1]) == 1:
                cnt += 1
                length = len(str(B))
                n = int(str(B)[:length - 1])
                B = n
            else:
                return -1
                
            if n == A:
                return cnt + 1
        except:
            return -1
        
print(cal(A, B))