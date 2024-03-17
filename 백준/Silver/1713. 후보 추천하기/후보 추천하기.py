N = int(input())
student = int(input())
recommend = list(map(int, input().split()))

pic = []
cnt = [0] * 101

for num in recommend:
    cnt[num] += 1
    if num in pic:
        continue
    elif len(pic) < N:
        pic.append(num)
    else:
        min_v = 1000
        for i in range(len(pic)):
            if cnt[pic[i]] < min_v:
                min_v = cnt[pic[i]]
                erase = pic[i]
        else:
            pic.remove(erase)
            cnt[erase] = 0
            pic.append(num)
            
print(*sorted(pic))