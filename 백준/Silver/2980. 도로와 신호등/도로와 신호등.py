n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.append([l, 0, 0])

time = arr[0][0]
for i in range(n):
    check = time % (arr[i][1] + arr[i][2])
    if check <= arr[i][1]:
        time += arr[i][1] - check
    time += arr[i+1][0] - arr[i][0]

print(time)