import sys
from collections import deque
input = sys.stdin.readline

s = int(input())

answer = 1e9
queue = deque([])
queue.append([1, 0, 0])
visited = [[False] * (s+1) for _ in range(s+1)]
visited[1][0] = True
while queue:
    x, y, time = queue.popleft()
    if x == s:
        answer = min(answer, time)
        continue

    for i in range(3):
        nx, ny = x, y
        if i == 0:
            ny = x
        elif i == 1:
            nx += y
        elif i == 2:
            nx -= 1

        if 0 <= nx <= s and 0 <= ny <= s and not visited[nx][ny]:
            queue.append([nx, ny, time+1])
            visited[nx][ny] = True

print(answer)