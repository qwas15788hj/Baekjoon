t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y, num = 0, 0, 1
    arr[x][y] = num
    target = n**2
    while True:
        for i in range(4):
            while True:
                x += dx[i]
                y += dy[i]
                if x<0 or x>=n or y<0 or y>=n or arr[x][y] != 0:
                    x -= dx[i]
                    y -= dy[i]
                    break
                else:
                    num += 1
                    arr[x][y] = num
        if num == target:
            break
        
    print("#{}" .format(tc))
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()