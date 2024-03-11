p, m = map(int, input().split())
arr = []
level = dict()
check = []
for _ in range(p):
    l, n = map(str, input().split())
    l = int(l)
    if len(arr) == 0:
        arr.append([n])
        level[n] = l
        check.append(l)
    else:
        for i in range(len(arr)):
            if len(arr[i]) < m and abs(check[i] - l) <= 10:
                arr[i].append(n)
                level[n] = l
                break
        else:
            arr.append([n])
            level[n] = l
            check.append(l)

for i in range(len(arr)):
    arr[i].sort()

for i in range(len(arr)):
    if len(arr[i]) == m:
        print("Started!")
    else:
        print("Waiting!")
    for j in range(len(arr[i])):
        print(level[arr[i][j]], arr[i][j])