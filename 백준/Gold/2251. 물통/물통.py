from collections import deque

a, b, c = map(int, input().split())
queue = deque()
visited = [[False] * (b+1) for _ in range(a+1)]
queue.append([0, 0])
visited[0][0] = True

answer = []

def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        queue.append([x, y])

while queue:
    x, y = queue.popleft()
    z = c - x - y
    if x == 0:
        answer.append(z)

    # x -> y
    water = min(x, b-y)
    pour(x-water, y+water)
    # x -> z
    water = min(x, c-z)
    pour(x-water, y)
    # y -> x
    water = min(y, a-x)
    pour(x+water, y-water)
    # y -> z
    water = min(y, c-z)
    pour(x, y-water)
    # z -> x
    water = min(z, a-x)
    pour(x+water, y)
    # z -> y
    water = min(z, b-y)
    pour(x, y+water)

answer.sort()
print(*answer)