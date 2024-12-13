n, k = map(int, input().split())
w, v = [0], [0]
for _ in range(n):
    a, b = map(int ,input().split())
    w.append(a)
    v.append(b)

arr = [[0]*(k+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        if w[i] <= j:
            # (지금 물품 넣기전 무게 + 지금 물품, 이전 물품)
            arr[i][j] = max(arr[i-1][j-w[i]] + v[i], arr[i-1][j])
        else:
            arr[i][j] = arr[i-1][j]

print(arr[-1][-1])