T = int(input())  # 스위치 개수
lst = list(map(int, input().split()))  # 스위치 상태, 인덱스 1~T
student = int(input())  # 학생 수

for i in range(student):
    gender, num = map(int, input().split())  # 학생 정보

    if gender == 1:  # 남학생
        for x in range(1, T + 1):
            if num * x <= T:  # 번호의 배수가 T 안에 있는 경우 스위치 바꿈
                a = num * x  # 스위치 배수를 저장
                if lst[a - 1] == 0:  # 0이면 1로
                    lst[a - 1] = 1
                elif lst[a - 1] == 1:  # 1이면 0으로
                    lst[a - 1] = 0


    elif gender == 2:  # 여학생
        num = num - 1  # 번호
        if lst[num] == 0:  # 0이면 1로
            lst[num] = 1
        elif lst[num] == 1:  # 1이면 0으로
            lst[num] = 0

        # 좌우 확인
        for x in range(1, T + 1):
            right = num + x  # 오른쪽
            left = num - x  # 왼쪽
            if 0 <= left and right < T and lst[right] == lst[left]:  # 좌우 스위치가 인덱스 안에 있고 대칭인 경우
                if lst[right] == 0:  # 0에서 1로
                    lst[right] = lst[left] = 1
                elif lst[right] == 1:  # 1에서 0으로
                    lst[right] = lst[left] = 0
            else:
                break

count = 0
for n in lst:  # 한 줄에 20개씩 출력
    print(n, end=' ')
    count += 1
    if count % 20 == 0:
        print()