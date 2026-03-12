from itertools import combinations
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

virus = []
count = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            virus.append([i, j])
        if arr[i][j] == 0:
            count += 1

# 바이러스 활성화 모든 경우의 수
comb = list(combinations(virus, m))
answer = 1e9
for com in comb:
    # 바이러스 활성화 경우 1가지씩 진행
    queue = deque([])
    visited = [[False] * n for _ in range(n)]
    for c in com:
        queue.append(c)
        visited[c[0]][c[1]] = True
        
    time = 0
    cnt = 0
    while queue and count != cnt:
        size = len(queue)
        for _ in range(size):
            x, y = queue.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 1 and not visited[nx][ny]:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                    if arr[nx][ny] == 0:
                        cnt += 1
                    
        time += 1

    # 모든 빈 칸에 바이러스를 퍼뜨렸는지 체크
    flag = True
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0 and not visited[i][j]:
                flag = False

    if flag:
        answer = min(answer, time)

if answer == 1e9:
    print(-1)
else:
    print(answer)