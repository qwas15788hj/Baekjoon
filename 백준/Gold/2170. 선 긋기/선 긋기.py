import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x:(x[0], x[1]))
answer, start = 0, -1e9
for i in range(n):
    if arr[i][1] > start:
        start = max(start, arr[i][0])
        answer += (arr[i][1] - start)
        start = arr[i][1]


print(int(answer))