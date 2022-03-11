n = int(input())
arr = list(map(int, input().split()))
m = int(input())

start = 0
end = max(arr)

result = 0
while start <= end:
    total = 0
    mid = (start+end)//2
    for i in arr:
        if i > mid:
            total += mid
        else:
            total += i
    if total <= m:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)