n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 0
for i in range(n):
    answer += arr[i][0] * arr[i][1]

print(answer)