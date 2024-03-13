n, k = map(int, input().split())
arr = list(map(int, input().split()))
number = [0] * (max(arr)+1)
left, right = 0, 0
answer = 0

while right < n:
    if number[arr[right]] < k:
        number[arr[right]] += 1
        right += 1
    else:
        number[arr[left]] -= 1
        left += 1

    answer = max(answer, right-left)

print(answer)