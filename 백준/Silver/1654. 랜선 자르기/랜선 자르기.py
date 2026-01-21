import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))
arr.sort()

start = 1
end = max(arr)
answer = 0
while start <= end:
    count = 0
    mid = (start+end)//2
    for i in arr:
        if i >= mid:
            count += i//mid
            
    if count < n:
        end = mid-1
    else:
        answer = mid
        start = mid+1
print(answer)