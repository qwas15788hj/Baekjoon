n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)
answer = 0
for i in range(n):
    answer += max(arr[i] - i, 0)

print(answer)