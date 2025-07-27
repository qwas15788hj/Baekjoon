n = int(input())
arr = list(map(int, input().split()))

left, right = 0, n-1
answer = 1e9
while left != right:
    check = arr[left] + arr[right]
    if abs(check) < abs(answer):
        answer = check

    if check < 0:
        left += 1
    else:
        right -= 1

print(answer)