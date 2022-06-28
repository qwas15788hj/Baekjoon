n = int(input())
arr = list(map(int, input().split()))
arr.sort()

for i in range(len(arr)):
    arr[i] -= i

print(1+max(arr)+n)