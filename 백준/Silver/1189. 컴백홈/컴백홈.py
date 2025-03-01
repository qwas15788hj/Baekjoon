import copy, sys
from collections import deque
input = sys.stdin.readline

r, c, k = map(int, input().split())
arr = [list(input()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque([])
v = [[False] * c for _ in range(r)]
v[r-1][0] = True
queue.append([r-1, 0, v, 1])

answer= 0
while queue:
    x, y, visited, count = queue.popleft()
    if x == 0 and y == c-1:
        if count == k:
            answer += 1
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and arr[nx][ny] == ".":
                sub_visited = copy.deepcopy(visited)
                sub_visited[nx][ny] = True
                queue.append([nx, ny, sub_visited, count+1])

print(answer)