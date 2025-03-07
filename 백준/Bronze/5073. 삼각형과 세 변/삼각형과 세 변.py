while True:
    x, y, z = map(int, input().split())
    if x == 0 and y == 0 and z == 0:
        break

    if x == y == z:
        print('Equilateral')
    else:
        max_val = max(x, y, z)
        if max_val < x + y + z - max_val:
            if x == y or y == z or x == z:
                print('Isosceles')
            else:
                print('Scalene')
        else:
            print('Invalid')