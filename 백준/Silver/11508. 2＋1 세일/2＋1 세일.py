n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)

result = 0
for i in range(2, len(arr), 3):
    result += arr[i]

print(sum(arr) - result)