n = int(input())
arr = [0] * (100001)
arr[1] = 3
arr[2] = 7
for i in range(3, n+1):
    arr[i] = (arr[i-1]*2 + arr[i-2])%9901

print(arr[n]%9901)