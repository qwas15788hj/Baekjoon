n, k = map(int, input().split())
arr = [[1], [1, 1]]
for i in range(2, n):
    check = [1]
    for j in range(i-1):
        check.append(arr[i-1][j] + arr[i-1][j+1])
    check.append(1)
    arr.append(check)

print(arr[n-1][k-1])