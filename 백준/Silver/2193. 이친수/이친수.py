n = int(input())
arr = [0] * 91
arr[1], arr[2] = 1, 1
for i in range(3, n+1):
    arr[i] = arr[i-2] + arr[i-1]

print(arr[n])