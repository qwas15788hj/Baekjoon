n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

start, end = min(arr), sum(arr)
answer = 1e9
while start <= end:
    mid = (start + end)//2
    money, count = mid, 1

    for i in range(n):
        if money < arr[i]:
            money = mid
            count += 1
        money -= arr[i]

    if count > m or mid < max(arr):
        start = mid + 1
    else:
        end = mid - 1
        answer = mid

print(answer)