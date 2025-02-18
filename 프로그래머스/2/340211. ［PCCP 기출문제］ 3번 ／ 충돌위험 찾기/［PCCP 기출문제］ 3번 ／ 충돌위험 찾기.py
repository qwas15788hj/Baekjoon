def solution(points, routes):
    answer = 0
    
    visited = []
    for route in routes:
        visit = []
        visit.append([points[route[0]-1][0], points[route[0]-1][1]])
        if len(route) != 1:
            for i in range(len(route)-1):
                x, y = points[route[i]-1][0], points[route[i]-1][1]
                nx, ny = points[route[i+1]-1][0], points[route[i+1]-1][1]
                count_x, count_y = abs(x-nx), abs(y-ny)
                # 세로 이동
                if count_x != 0:
                    if x > nx:
                        for _ in range(count_x):
                            x -= 1
                            visit.append([x, y])
                    else:
                        for _ in range(count_x):
                            x += 1
                            visit.append([x, y])
                # 가로 이동
                if count_y != 0:
                    if y > ny:
                        for _ in range(count_y):
                            y -= 1
                            visit.append([x, y])
                    else:
                        for _ in range(count_y):
                            y += 1
                            visit.append([x, y])
                            
        visited.append(visit)
    
    
    n = len(visited)
    m = 0
    for i in visited:
        m = max(m, len(i))
    
    for i in range(m):
        check = []
        idx = set()
        for j in range(n):
            if len(visited[j]) > i:
                if [visited[j][i][0], visited[j][i][1]] in check:
                    idx.add((visited[j][i][0], visited[j][i][1]))
                else:
                    check.append([visited[j][i][0], visited[j][i][1]])
    
        answer += len(idx)
                    
    return answer