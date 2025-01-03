n = int(input())
arr = list(map(int, input().split()))

answer = 0
start, end = 0, 0
while True:
    if end == n:
        break

    if start == end:
        end += 1
        continue

    if arr[start] >= arr[end]:
        start = end
    else:
        answer = max(answer, arr[end] - arr[start])
        end += 1

print(answer)