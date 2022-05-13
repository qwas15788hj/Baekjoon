import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)
answer = 0
while start <= end:
    count = 0
    mid = (start+end)//2
    for i in arr:
        if i > mid:
            count += i-mid
    if count < m:
        end = mid-1
    else:
        start = mid+1
        answer = mid
print(answer)