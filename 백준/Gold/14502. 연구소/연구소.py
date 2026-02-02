from collections import deque
from itertools import combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(list):
    SubArr = [i[:] for i in arr]
    for li in list:
        SubArr[li[0]][li[1]] = 1

    queue = deque()
    for i in range(n):
        for j in range(m):
            if(arr[i][j]==2):
                queue.append([i, j])

    while queue:
        size = len(queue)
        for i in range(size):
            x, y = queue.popleft()
            for j in range(4):
                nx = x+dx[j]
                ny = y+dy[j]
                if(0<=nx<n and 0<=ny<m and SubArr[nx][ny]==0):
                    SubArr[nx][ny] = 2
                    queue.append([nx, ny])

    count = 0
    for i in range(n):
        for j in range(m):
            if SubArr[i][j]==0:
                count += 1

    global answer
    answer = max(answer, count)


n, m = map(int, input().split())
answer = 0
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

lists = []
for i in range(n):
    for j in range(m):
        if(arr[i][j]==0):
            lists.append([i, j])

list = combinations(lists, 3)

for li in list:
    bfs(li)

print(answer)