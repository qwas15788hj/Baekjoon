import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
answer = [arr[0], arr[-1]]
for i in range(n):
    if arr[i] < 0:
        start, end = max(0, i-1), n-1
    else:
        start, end = 0, min(n-1, i+1)

    while start <= end:
        mid = (start + end) // 2
        if i != mid and abs(arr[i] + arr[mid]) < abs(sum(answer)):
            answer = [min(arr[i], arr[mid]), max(arr[i], arr[mid])]

        if arr[i] + arr[mid] < 0:
            start = mid + 1
        else:
            end = mid - 1

print(*answer)