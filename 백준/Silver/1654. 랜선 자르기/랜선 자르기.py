import sys

k, n = map(int, sys.stdin.readline().split())
array = []
for _ in range(k):
    array.append(int(sys.stdin.readline()))
    
start = 1
end = max(array)

result = 0
while start<=end:
    total = 0
    mid = (start+end) // 2
    for i in array:
        if i >= mid:
            total += i//mid
    if total < n:
        end = mid - 1
    else:
        start = mid + 1
        result = mid
print(result)