n, m = map(int, input().split())
arr = list(map(int, input().split()))
num, left = 0, 0
answer = 0

for i in range(n):
    num += arr[i]
    while num > m:
        num -= arr[left]
        left += 1

    if num == m:
        answer += 1

print(answer)