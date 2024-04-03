n = int(input())
arr = list(map(int, input().split()))
arr.sort()
left, right = 0, n-1
answer = [0, 0]
check = 2000000001

while left != right:
    if abs(arr[left] + arr[right]) < check:
        check = abs(arr[left] + arr[right])
        answer[0], answer[1] = arr[left], arr[right]

    if arr[left] + arr[right] >= 0:
        right -= 1
    else:
        left += 1

print(*answer, end=" ")