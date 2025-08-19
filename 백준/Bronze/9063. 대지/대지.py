n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

min_x, max_x, min_y, max_y = 1e9, -1e9, 1e9, -1e9
for x, y in arr:
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

print((max_x-min_x) * (max_y-min_y))