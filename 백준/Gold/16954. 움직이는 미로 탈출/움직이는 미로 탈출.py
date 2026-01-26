from collections import deque

arr = [list(input()) for _ in range(8)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1, 0]
dy = [0, 1, 1, 1, 0, -1, -1, -1, 0]

queue = deque([])
queue.append([7, 0])
flag = False
while queue:
    # 벽 이동 전 캐릭터 이동
    sub_queue = set()
    size = len(queue)
    for _ in range(size):
        x, y = queue.popleft()
        if x == 0 and y == 7:
            flag = True
            break
        for k in range(9):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 8 and 0 <= ny < 8 and arr[nx][ny] == '.':
                sub_queue.add((nx, ny))
                
    if flag:
        break
        
    # 벽 이동 (아래부터)
    for i in range(8):
        arr[-1][i] = '.'
    for i in range(6, -1, -1):
        for j in range(8):
            # 벽 이동
            if arr[i][j] == '#':
                arr[i+1][j] = '#'
                arr[i][j] = '.'
                if (i+1, j) in sub_queue: # 벽 위치에 캐릭터 있다면 삭제
                    sub_queue.remove((i+1, j))

    queue = deque(sub_queue)

if flag:
    print(1)
else:
    print(0)