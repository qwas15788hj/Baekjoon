n = int(input())
arr = list(map(int, input().split()))

num = sum(arr)
answer = 0
for i in range(n-1):
    num -= arr[i]
    answer += arr[i] * num

print(answer)