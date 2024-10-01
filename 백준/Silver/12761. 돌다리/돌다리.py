from collections import deque

a, b, n, m = map(int, input().split())

dx = [-1, 1, -a, a, -b, b, a, b]
queue = deque([])
queue.append(n)
visited = [0] * 100001
visited[n] = 1

while queue:
    x = queue.popleft()
    for i in range(8):
        if i < 6:
            if 0 <= x+dx[i] < 100001 and visited[x+dx[i]] == 0:
                queue.append(x+dx[i])
                visited[x+dx[i]] = visited[x] + 1
        else:
            if 0 <= x*dx[i] < 100001 and visited[x*dx[i]] == 0:
                queue.append(x*dx[i])
                visited[x*dx[i]] = visited[x] + 1

print(visited[m]-1)