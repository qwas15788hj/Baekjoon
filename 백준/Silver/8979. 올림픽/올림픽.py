n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    if arr[i][0] == k:
        g, s, b = arr[i][1], arr[i][2], arr[i][3]
        break

arr.sort(key=lambda x:(-x[1], -x[2], -x[3]))

rank = 0
for i in range(n):
    if arr[i][1] == g and arr[i][2] == s and arr[i][3] == b:
        break
    else:
        rank += 1

print(rank + 1)