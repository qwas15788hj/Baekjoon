a, b = map(int, input().split())
n = int(input())
arr = [int(input()) for _ in range(n)]

answer = abs(a - b)
for i in range(len(arr)):
    answer = min(answer, abs(arr[i] - b) + 1)

print(answer)