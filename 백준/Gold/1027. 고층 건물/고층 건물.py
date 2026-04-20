n = int(input())
arr = list(map(int, input().split()))

answer = 0
for i in range(n):
    left, right = arr[:i][::-1], arr[i+1:]
    max_slope = -1e9
    result = 0
    for j in range(len(left)):
        slope = (left[j]-arr[i])/(j+1)
        if slope > max_slope:
            max_slope = slope
            result += 1

    max_slope = -1e9
    for j in range(len(right)):
        slope = (right[j]-arr[i])/(j+1)
        if slope > max_slope:
            max_slope = slope
            result += 1

    answer = max(answer, result)

print(answer)