while True:
    x, y, z = map(int, input().split())
    if x == 0 and y == 0 and z == 0:
        break

    if max(x, y, z) >= x + y + z - max(x, y, z):
        print("Invalid")
    else:
        if x == y and y == z:
            print("Equilateral")
        elif (x == y and x != z) or (x == z and x != y) or (y == z and x != y):
            print("Isosceles")
        else:
            print("Scalene")