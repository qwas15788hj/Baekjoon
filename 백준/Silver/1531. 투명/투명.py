n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
paper = [[0] * 100 for _ in range(100)]

for i in range(n):
    sx, sy = arr[i][0], arr[i][1]
    ex, ey = arr[i][2], arr[i][3]
    for x in range(sx-1, ex):
        for y in range(sy-1, ey):
            paper[x][y] += 1

answer = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] > m:
            answer += 1

print(answer)