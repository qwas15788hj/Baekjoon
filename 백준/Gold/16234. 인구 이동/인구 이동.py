from collections import deque

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, check):
    queue = deque([[i, j]])
    visited[i][j] = check
    city[check] = 1
    person[check] = arr[x][y]
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and l <= abs(arr[nx][ny] - arr[x][y]) <= r and visited[nx][ny] == 0:
                queue.append([nx, ny])
                visited[nx][ny] = check
                city[check] += 1
                person[check] += arr[nx][ny]

flag = True
answer = 0
while flag:
    visited = [[0] * n for _ in range(n)]
    check = 1
    city = dict()
    person = dict()
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                bfs(i, j, check)
            check += 1
            
    if len(city) == n**2:
        flag = False
    for i in range(n):
        for j in range(n):
            idx = visited[i][j]
            arr[i][j] = person[idx]//city[idx]
            
    answer += 1

print(answer-1)