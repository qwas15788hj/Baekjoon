import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
answer = 0
for i in range(n-1):
    idx1, idx2 = -1, -1
    start, end = i+1, n-1
    while start <= end:
        mid = (start + end)//2

        if arr[mid]*0.9 > arr[i]:
            end = mid - 1
        elif arr[mid] < arr[i]:
            start = mid + 1
        elif arr[mid]*0.9 <= arr[i] <= arr[mid]:
            end = mid - 1
            idx1 = mid

    start, end = i+1, n-1
    while start <= end:
        mid = (start + end)//2

        if arr[mid]*0.9 > arr[i]:
            end = mid - 1
        elif arr[mid] < arr[i]:
            start = mid + 1
        elif arr[mid]*0.9 <= arr[i] <= arr[mid]:
            start = mid + 1
            idx2 = mid

    if idx1 != -1 and idx2 != -1:
        answer += idx2-idx1+1

print(answer)