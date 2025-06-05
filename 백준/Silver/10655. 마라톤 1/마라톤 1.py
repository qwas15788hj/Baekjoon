n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

total = 0
for i in range(n-1):
    total += abs(arr[i][0]-arr[i+1][0]) + abs(arr[i][1]-arr[i+1][1])

answer = 1e9
for i in range(1, n-1):
    dist1 = abs(arr[i-1][0]-arr[i][0]) + abs(arr[i-1][1]-arr[i][1])
    dist2 = abs(arr[i][0]-arr[i+1][0]) + abs(arr[i][1]-arr[i+1][1])
    dist3 = abs(arr[i-1][0]-arr[i+1][0]) + abs(arr[i-1][1]-arr[i+1][1])
    answer = min(answer, total-dist1-dist2+dist3)

print(answer)