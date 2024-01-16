n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
pipe = [[[0] * 3 for _ in range(n)] for _ in range(n)]

pipe[0][1][0] = 1
for i in range(n):
    for j in range(1, n):
        if i == 0 and j == 1:
            continue
        if arr[i][j] == 0:
            pipe[i][j][0] = pipe[i][j-1][0] + pipe[i][j-1][2]
            pipe[i][j][1] = pipe[i-1][j][1] + pipe[i-1][j][2]
            if arr[i-1][j] == 0 and arr[i][j-1] == 0:
                pipe[i][j][2] = pipe[i-1][j-1][0] + pipe[i-1][j-1][1] + pipe[i-1][j-1][2]

print(sum(pipe[n-1][n-1]))