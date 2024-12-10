n = int(input())
arr = list(map(int, input().split()))
arr.sort()

size = sum(arr)
answer = 0
for i in range(n-1):
    size -= arr[i]
    answer += arr[i] * size

print(answer)