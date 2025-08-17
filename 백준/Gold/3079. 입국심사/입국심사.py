import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

INF = 10**18
start, end = 0, INF
answer = INF
while start <= end:
    mid = (start+end)//2
    count = 0
    for i in range(len(arr)):
        count += mid//arr[i]

    if count >= m:
        end = mid-1
        answer = min(answer, mid)
    else:
        start = mid+1

print(answer)