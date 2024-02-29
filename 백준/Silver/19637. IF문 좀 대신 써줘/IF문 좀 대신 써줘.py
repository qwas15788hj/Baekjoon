import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(n):
    a, b = map(str, input().split())
    arr.append([a, int(b)])

arr.sort(key=lambda x:x[1])

for i in range(m):
    power = int(input())
    start, end = 0, len(arr)
    answer = 0
    while start <= end:
        mid = (start+end)//2
        if int(arr[mid][1]) >= power:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1

    print(arr[answer][0])