n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
check = [0] * n

for i in range(n):
    dic = dict()
    count = 0
    for j in range(n):
        if i == j:
            continue
        if j in dic:
            continue
        for k in range(5):
            if arr[i][k] == arr[j][k]:
                dic[j] = 0
                count += 1
                break

    check[i] = count

print(check.index(max(check)) + 1)