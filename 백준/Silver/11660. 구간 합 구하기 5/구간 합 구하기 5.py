import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0]*(n+1)]
for _ in range(n):
    a = list(map(int, input().split()))
    arr.append([0]+a)

sum_arr = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        sum_arr[i][j] = sum_arr[i-1][j]+sum_arr[i][j-1]-sum_arr[i-1][j-1]+arr[i][j]

answer = []
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    target = sum_arr[x2][y2] - sum_arr[x2][y1-1] - sum_arr[x1-1][y2] + sum_arr[x1-1][y1-1]
    answer.append(target)

for i in answer:
    print(i)