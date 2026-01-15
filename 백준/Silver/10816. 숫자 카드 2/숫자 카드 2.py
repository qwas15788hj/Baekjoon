import sys
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()
answer = []
for i in range(m):
    right = -1
    start, end = 0, n
    while start <= end:
        mid = (start+end)//2
        if mid >= n:
            break

        if arr1[mid] == arr2[i]:
            right = mid
            start = mid + 1
        if arr1[mid] < arr2[i]:
            start = mid + 1
        if arr1[mid] > arr2[i]:
            end = mid - 1

    left = -1
    start, end = 0, n
    while start <= end:
        mid = (start+end)//2
        if mid >= n:
            break

        if arr1[mid] == arr2[i]:
            left = mid
            end = mid - 1
        if arr1[mid] < arr2[i]:
            start = mid + 1
        if arr1[mid] > arr2[i]:
            end = mid - 1

    if left != -1:
        answer.append(right - left + 1)
    else:
        answer.append(0)

print(*answer)