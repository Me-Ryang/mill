N = int(input())
lst = []
for i in range(N):
    lst.append(int(input()))

num = 0
for i in range(N-1, 0, -1): # 뒤에서부터 비교
    if lst[i] <= lst[i-1]: # 마지막 값보다 그 앞 값이 큰 경우
        tmp = lst[i-1]
        lst[i-1] = lst[i]-1 # 마지막 값보다 작은 값 넣음
        num += tmp - lst[i-1]

print(num)