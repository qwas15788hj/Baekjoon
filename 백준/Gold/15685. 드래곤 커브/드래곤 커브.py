n = int(input())

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
visited = [[0] * 101 for _ in range(101)]
for _ in range(n):
    y, x, d, g = map(int, input().split())
    arr = [d]
    for i in range(g):
        size = len(arr)
        for j in range(size-1, -1, -1):
            arr.append((arr[j]+1)%4)

    visited[x][y] = 1
    for i in range(len(arr)):
        x += dx[arr[i]]
        y += dy[arr[i]]
        visited[x][y] = 1

answer = 0
for i in range(100):
    for j in range(100):
        if (visited[i][j] + visited[i+1][j] + visited[i][j+1] + visited[i+1][j+1]) == 4:
            answer += 1

print(answer)