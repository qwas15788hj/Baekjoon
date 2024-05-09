from collections import deque

arr = [list(input()) for _ in range(12)]
answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    num = 0
    visited = [[0] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if arr[i][j] != "." and visited[i][j] == 0:
                num += 1
                queue = deque()
                queue.append([i, j])
                visited[i][j] = num
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < 12 and 0 <= ny < 6 and arr[nx][ny] == arr[i][j] and visited[nx][ny] == 0:
                            queue.append([nx, ny])
                            visited[nx][ny] = num

    return visited

def move():
    for j in range(6):
        for i in range(11, -1, -1):
            if arr[i][j] != ".":
                for z in range(11, i, -1):
                    if arr[z][j] == ".":
                        arr[i][j], arr[z][j] = arr[z][j], arr[i][j]
                        break

while True:
    visited = bfs()
    max_num = -1e9
    for v in visited:
        max_num = max(max_num, max(v))

    num_arr = [0] * (max_num + 1)
    for i in range(len(visited)):
        for j in range(len(visited[i])):
            if visited[i][j] != 0:
                num_arr[visited[i][j]] += 1

    if max(num_arr) >= 4:
        for i in range(len(visited)):
            for j in range(len(visited[i])):
                if visited[i][j] != 0 and num_arr[visited[i][j]] >= 4:
                    arr[i][j] = "."

        move()
        answer += 1

    else:
        break

print(answer)