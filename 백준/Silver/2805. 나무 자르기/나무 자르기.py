n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start+end) // 2
    for i in array:
        if i > mid:
            total += i-mid
    if total < m:
        end = mid - 1
    else:
        start = mid + 1
        result = mid
print(result)