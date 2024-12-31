n = int(input())
arr = [0]
for i in range(1, n):
    arr.append(arr[-1] + i)

print(arr[n-1])