from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
queue = deque([])
queue.append([r1, c1])
visited = [[0] * n for _ in range(n)]
visited[r1][c1] = 1

while queue:
    x, y = queue.popleft()
    for i in range(6):
        if 0 <= x+dx[i] < n and 0 <= y+dy[i] < n and visited[x+dx[i]][y+dy[i]] == 0:
            queue.append([x+dx[i], y+dy[i]])
            visited[x+dx[i]][y+dy[i]] = visited[x][y] + 1

print(visited[r2][c2]-1)