n = int(input())
arr = [list(input()) for _ in range(n)]

max_x, min_x, max_y, min_y = 0, 1e9, 0, 1e9
count = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            max_x = max(max_x, i)
            min_x = min(min_x, i)
            max_y = max(max_y, j)
            min_y = min(min_y, j)
            count += 1

answer = 1e9

if count == 1:
    answer = 0

for i in range(n):
    if arr[i].count('G') == count:
        answer = min(max_y, (n-1)-min_y)

for j in range(n):
    cnt = 0
    for i in range(n):
        if arr[i][j] == 'G':
            cnt += 1
    if cnt == count:
        answer = min(max_x, (n-1)-min_x)

# 왼쪽위 [0, 0]
# 오른쪽위 [0, n-1]
# 왼쪽아래 [n-1, 0]
# 오른쪽아래 [n-1, n-1]
target = [[0, 0] for _ in range(4)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            target[0][0], target[0][1] = max(target[0][0], i), max(target[0][1], j)
            target[1][0], target[1][1] = max(target[1][0], i), max(target[1][1], (n-1)-j)
            target[2][0], target[2][1] = max(target[2][0], (n-1)-i), max(target[2][1], j)
            target[3][0], target[3][1] = max(target[3][0], (n-1)-i), max(target[3][1], (n-1)-j)

if count == 1:
    answer = 0
for t in target:
    answer = min(answer, sum(t))

print(answer)