from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

x, y = 0, 0
queue = deque()
queue.append([x, y])
visited = [[False] * n for _ in range(n)]
visited
flag = False
while queue:
    nx, ny = queue.popleft()
    if nx == n-1 and ny == n-1:
        flag = True
        break

    num = arr[nx][ny]
    if 0 <= nx+num < n and not visited[nx+num][ny]:
        queue.append([nx+num, ny])
        visited[nx+num][ny] = True
    if 0 <= ny+num < n and not visited[nx][ny+num]:
        queue.append([nx, ny+num])
        visited[nx][ny+num] = True

if flag:
    print("HaruHaru")
else:
    print("Hing")