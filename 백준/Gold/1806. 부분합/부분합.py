n, s = map(int, input().split())
arr = [0] + list(map(int, input().split()))

for i in range(1, n+1):
    arr[i] += arr[i-1]

answer = 1e9
left, right = 0, 1
while right < len(arr):
    num = arr[right] - arr[left]
    if num >= s:
        answer = min(answer, right - left)
        left += 1
    else:
        right += 1

if answer == 1e9:
    print(0)
else:
    print(answer)