import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, a, b = map(int, input().split())
    arr[x-1][y-1].append([a-1, b-1])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append([0, 0])
light = [[False] * n for _ in range(n)] # 불 킨 방
visited = [[False] * n for _ in range(n)] # 실제 방문 한 방
light[0][0] = True
visited[0][0] = True
while queue:
    x, y = queue.popleft()
    # 불 키기
    for a, b in arr[x][y]:
        if not light[a][b]:
            light[a][b] = True
            # 새로 불 켠 방이 '이미 방문한 방'과 인접하면 방문 가능
            for k in range(4):
                na, nb = a + dx[k], b + dy[k]
                if 0 <= na < n and 0 <= nb < n and visited[na][nb]:
                    queue.append([a, b])
                    visited[a][b] = True
                    break

    # 인접한 방 방문하기
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and light[nx][ny] and not visited[nx][ny]:
            queue.append([nx, ny])
            visited[nx][ny] = True

answer = 0
for l in light:
    answer += l.count(True)
print(answer)