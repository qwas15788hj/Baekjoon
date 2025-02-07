def solution(park, routes):
    x, y = 0, 0
    n, m = len(park), len(park[0])
    for i in range(n):
        for j in range(m):
            if park[i][j] == "S":
                x, y = i, j
                break
    
    dx = [-1, 1, 0 ,0]
    dy = [0, 0, -1, 1]
    for route in routes:
        rou = route.split(" ")
        dire, count = rou[0], int(rou[1])
        
        nx, ny = x, y
        flag = True
        # 북쪽
        if dire == "N":
            for _ in range(count):
                nx += dx[0]
                if nx < 0 or park[nx][ny] == "X":
                    flag = False
                    break
        # 남쪽
        elif dire == "S":
            for _ in range(count):
                nx += dx[1]
                if nx >= n or park[nx][ny] == "X":
                    flag = False
                    break
        # 서쪽
        elif dire == "W":
            for _ in range(count):
                ny += dy[2]
                if ny < 0 or park[nx][ny] == "X":
                    flag = False
                    break
        # 동쪽
        elif dire == "E":
            for _ in range(count):
                ny += dy[3]
                if ny >= m or park[nx][ny] == "X":
                    flag = False
                    break
        
        if flag:
            x, y = nx, ny
    
    return [x, y]