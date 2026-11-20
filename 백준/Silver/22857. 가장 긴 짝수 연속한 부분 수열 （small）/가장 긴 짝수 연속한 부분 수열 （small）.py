n, m = map(int, input().split())
arr = list(map(int, input().split()))

left, odd, even, answer = 0, 0, 0, 0
for i in range(n):
    if arr[i]%2 != 0:
        odd += 1
    else:
        even += 1

    while odd > m:
        if arr[left]%2 != 0:
            odd -= 1
        else:
            even -= 1
        left += 1

    answer = max(answer, even)

print(answer)