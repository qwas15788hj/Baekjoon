n, m = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, max(arr)
answer = 0
while start <= end:
    mid = (start+end)//2
    count = 0
    for i in range(n):
        if arr[i] > mid:
            count += (arr[i] - mid)
            
    if count >= m:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)