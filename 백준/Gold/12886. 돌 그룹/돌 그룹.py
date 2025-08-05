import sys
input = sys.stdin.readline
from collections import deque

a, b, c = map(int, input().split())

total = a+b+c
if total%3 != 0:
    print(0)
    exit()

a, b, c = sorted([a, b, c])
queue = deque()
visited = [[False] * total for _ in range(total)]
queue.append([a, b])
visited[a][b] = True

answer = 0
while queue:
    x, y = queue.popleft()
    z = total - (x+y)
    if x == y and y == z:
        answer = 1
        break

    arr = [x, y, z]
    for i in range(3):
        for j in range(3):
            if i == j:
                continue

            nx, ny = arr[i], arr[j]
            if nx > ny:
                nx -= ny
                ny += ny
                nz = total - (nx + ny)
                narr = sorted([nx, ny, nz])
                if not visited[narr[0]][narr[1]]:
                    queue.append([narr[0], narr[1]])
                    visited[narr[0]][narr[1]] = True

print(answer)