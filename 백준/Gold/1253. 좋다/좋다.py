n = int(input())
arr = list(map(int, input().split()))

arr.sort()
answer = 0
for i in range(n):
    target = arr[i]
    sub_arr = arr[:i] + arr[i+1:]
    left, right = 0, len(sub_arr)-1

    while left < right:
        total = sub_arr[left] + sub_arr[right]
        if total > target:
            right -= 1
        elif total < target:
            left += 1
        elif total == target:
            answer += 1
            break

print(answer)