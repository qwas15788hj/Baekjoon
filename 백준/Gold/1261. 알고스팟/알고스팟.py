import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
queue.append([0, 0])
visited = [[1e9] * n for _ in range(m)] # 벽 부순 최소 횟수 저장
visited[0][0] = 0 # 시작점
while queue:
    x, y = queue.popleft()
    if x == m-1 and y == n-1:
        continue

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < m and 0 <= ny < n:
            # 다음 칸이 길(0)인 경우
            if arr[nx][ny] == 0 and visited[x][y] < visited[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = visited[x][y]
            # 다음 칸이 벽(1)인 경우
            elif arr[nx][ny] == 1 and visited[x][y]+1 < visited[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = visited[x][y]+1

print(visited[-1][-1])