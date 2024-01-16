import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
pipe = [[[] for _ in range(n)] for _ in range(n)]
pipe[0][1].append(1)

for i in range(n):
    for j in range(n):
        for z in range(len(pipe[i][j])):
            if pipe[i][j][z] == 1:
                if j+1 < n and arr[i][j+1] == 0:
                    pipe[i][j+1].append(1)
                if j+1 < n and i+1 < n and arr[i][j+1] == 0 and arr[i+1][j] == 0 and arr[i+1][j+1] == 0:
                    pipe[i+1][j+1].append(2)
            elif pipe[i][j][z] == 2:
                if j+1 < n and arr[i][j+1] == 0:
                    pipe[i][j+1].append(1)
                if j+1 < n and i+1 < n and arr[i][j+1] == 0 and arr[i+1][j] == 0 and arr[i+1][j+1] == 0:
                    pipe[i+1][j+1].append(2)
                if i+1 < n and arr[i+1][j] == 0:
                    pipe[i+1][j].append(3)
            else:
                if j+1 < n and i+1 < n and arr[i][j+1] == 0 and arr[i+1][j] == 0 and arr[i+1][j+1] == 0:
                    pipe[i+1][j+1].append(2)
                if i+1 < n and arr[i+1][j] == 0:
                    pipe[i+1][j].append(3)

print(len(pipe[n-1][n-1]))