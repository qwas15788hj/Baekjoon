n, m = map(int, input().split())
arr = list(map(int, input().split()))

start, end = max(arr), sum(arr)
answer = 1e9
while start <= end:
    mid = (start + end)//2
    size = 0
    count = 0
    for i in range(n):
        if size + arr[i] > mid:
            size = arr[i]
            count += 1
        else:
            size += arr[i]
    if size != 0:
        count += 1

    if count > m:
        start = mid + 1
    else:
        answer = mid
        end = mid - 1

print(answer)