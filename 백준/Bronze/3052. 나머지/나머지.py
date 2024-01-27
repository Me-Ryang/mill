number = []
for _ in range(10):
    num = int(input()) % 42
    number.append(num)
    
set_number = set(number)
print(len(set_number))