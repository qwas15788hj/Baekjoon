n = int(input())
arr = list(map(int, input().split()))

arr.sort()
answer = 0
for i in range(n):
    sub_arr = arr[:i] + arr[i+1:]
    left, right = 0, len(sub_arr)-1

    while left < right:
        total = sub_arr[left] + sub_arr[right]
        if total < arr[i]:
            left += 1
        elif total > arr[i]:
            right -= 1
        else:
            answer += 1
            break

print(answer)