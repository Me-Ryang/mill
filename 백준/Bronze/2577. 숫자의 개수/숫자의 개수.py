num_list = []
for _ in range(3):
    num = int(input())
    num_list.append(num)
    
multi = list(map(int, str(num_list[0] * num_list[1] * num_list[2])))

for i in range(0, 10):
    print(multi.count(i))