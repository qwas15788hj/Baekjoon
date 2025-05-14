n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort()
time = 0
for i in range(n):
    time = max(time, arr[i][0])
    time += arr[i][1]

print(time)