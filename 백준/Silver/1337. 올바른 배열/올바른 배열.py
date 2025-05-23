n = int(input())
arr = [int(input()) for _ in range(n)]

arr.sort()
left, right = 0, 0
answer = 4
while True:
    if right == n:
        break

    if arr[left]+4 < arr[right]:
        answer = min(answer, 5-(right-left))
        left += 1
    else:
        right += 1
answer = min(answer, 5-(right-left))

print(answer)