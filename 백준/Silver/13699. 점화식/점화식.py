n = int(input())
arr = [0] * 36
arr[0] = 1
arr[1] = 1
arr[2] = 2
arr[3] = 5

for i in range(4, n+1):
    for j in range(i):
        arr[i] += arr[j] * arr[i-j-1]

print(arr[n])