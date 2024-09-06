n = int(input())
m = int(input())
arr = list(map(int, input().split()))
result = []

for i in range(m):
    flag = False
    for j in range(len(result)):
        if arr[i] == result[j][0]:
            result[j][1] += 1
            flag = True
            break

    if not flag:
        if len(result) < n:
            result.append([arr[i], 1, i])
        else:
            result.pop(0)
            result.append([arr[i], 1, i])

    result.sort(key=lambda x:(x[1], x[2]))

result.sort()
for i in range(len(result)):
    print(result[i][0], end=" ")