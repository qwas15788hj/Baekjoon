n, k, p, x = map(int, input().split())
arr = [
    [0, 4, 3, 3, 4, 3, 2, 3, 1, 2],
    [4, 0, 5, 3, 2, 5, 6, 1, 5, 4],
    [3, 5, 0, 2, 5, 4, 3, 4, 2, 3],
    [3, 3, 2, 0, 3, 2, 3, 2, 2, 1],
    [4, 2, 5, 3, 0, 3, 4, 3, 3, 2],
    [3, 5, 4, 2, 3, 0, 1, 4, 2, 1],
    [2, 6, 3, 3, 4, 1, 0, 5, 1, 2],
    [3, 1, 4, 2, 3, 4, 5, 0, 4, 3],
    [1, 5, 2, 2, 3, 2, 1, 4, 0, 1],
    [2, 4, 3, 1, 2, 1, 2, 3, 1, 0]
]

answer = 0
now = '0'*(k-len(str(x))) + str(x)
for i in range(1, n+1):
    target = '0'*(k-len(str(i))) + str(i)
    if now == target:
        continue

    count = 0
    for j in range(len(now)):
        count += arr[int(now[j])][int(target[j])]

    if count <= p:
        answer += 1

print(answer)