king, stone, cnt = input().split()

loc = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
dir = {
    'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1],
    'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]
}

x1 = loc[king[0]]
y1 = int(king[1]) - 1

x2 = loc[stone[0]]
y2 = int(stone[1]) - 1

king_x, king_y, stone_x, stone_y = 0, 0, 0, 0
count = int(cnt)
while count != 0:
    move = input()
    king_x = x1 + dir[move][0]
    king_y = y1 + dir[move][1]
    if 0 <= king_x < 8 and 0 <= king_y < 8:
        if king_x == x2 and king_y == y2:
            stone_x = x2 + dir[move][0]
            stone_y = y2 + dir[move][1]
            if 0 <= stone_x < 8 and 0 <= stone_y < 8:
                x1 = king_x
                y1 = king_y
                x2 = stone_x
                y2 = stone_y
        else:
            x1 = king_x
            y1 = king_y

    count -= 1

king = ''
stone = ''
for key, value in loc.items():
    if value == x1:
        king += key
    if value == x2:
        stone += key
king += str(y1 + 1)
stone += str(y2 + 1)

print(king)
print(stone)