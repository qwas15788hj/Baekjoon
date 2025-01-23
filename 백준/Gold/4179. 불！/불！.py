from collections import deque

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
arr.insert(0, [0] * c)
arr.append([0] * c)
for i in range(r+2):
    arr[i].insert(0, 0)
    arr[i].append(0)

# 지훈, 불 위치, 배열 초기화
j_queue = deque()
f_queue = deque()
for i in range(r+2):
    for j in range(c+2):
        if arr[i][j] == "#":
            arr[i][j] = -1
        elif arr[i][j] == "F":
            f_queue.append([i, j])
            arr[i][j] = -2
        elif arr[i][j] == "J":
            j_queue.append([i, j])
            arr[i][j] = 1
        else:
            arr[i][j] = 0

time = 0
n, m = len(arr), len(arr[0])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 1e9
while j_queue:
    # 불 이동
    size = len(f_queue)
    for _ in range(size):
        x, y = f_queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 1 <= nx < r+1 and 1 <= ny < c+1 and arr[nx][ny] >= 0:
                arr[nx][ny] = -2
                f_queue.append([nx, ny])

    # 지훈 이동
    size = len(j_queue)
    for _ in range(size):
        x, y = j_queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                arr[nx][ny] = time + 1
                j_queue.append([nx, ny])

    # 탈출 체크
    for i in range(m):
        if arr[0][i] > 0:
            answer = min(answer, arr[0][i])
        if arr[-1][i] > 0:
            answer = min(answer, arr[-1][i])
    for i in range(n):
        if arr[i][0] > 0:
            answer = min(answer, arr[i][0])
        if arr[i][-1] > 0:
            answer = min(answer, arr[i][-1])
    if answer != 1e9:
        break

    time += 1

if answer == 1e9:
    print("IMPOSSIBLE")
else:
    print(answer)