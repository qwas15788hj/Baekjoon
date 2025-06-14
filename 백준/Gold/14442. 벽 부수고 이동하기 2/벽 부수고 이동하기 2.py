import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]

# 네 방향 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 큐 생성
queue = deque([])
queue.append([0, 0, 0])

# 벽 부순 수를 체크하기 위해 n, m, (k+1)인 3차원 배열 생성
visited = [[[1e9] * (k+1) for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

while queue:
    x, y, c = queue.popleft()
    if x == n and y == m:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 다음 이동이 범위 안에 있으며
        if 0 <= nx < n and 0 <= ny < m:
            # 벽이 아니며, 아직 이동하지 않은 곳이면 이동
            # 벽을 부수지 않았기에, c는 그대로 이동
            if arr[nx][ny] == 0 and visited[nx][ny][c] == 1e9:
                queue.append([nx, ny, c])
                visited[nx][ny][c] = visited[x][y][c] + 1
            # 벽이지만, 벽을 뚫을 수 있다면 이동
            # 벽을 부수었기에, c+1로 이동
            elif arr[nx][ny] == 1 and k > c and visited[nx][ny][c+1] == 1e9:
                queue.append([nx, ny, c+1])
                visited[nx][ny][c+1] = visited[x][y][c] + 1

if min(visited[-1][-1]) != 1e9:
    print(min(visited[-1][-1]))
else:
    print(-1)