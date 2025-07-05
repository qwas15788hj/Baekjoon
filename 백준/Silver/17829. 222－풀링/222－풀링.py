n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def pooling(arr2):
    result = []
    k = len(arr2)
    for i in range(0, k, 2):
        row = []
        for j in range(0, k, 2):
            check = [arr2[i][j], arr2[i][j+1], arr2[i+1][j], arr2[i+1][j+1]]
            check.sort()
            row.append(check[2])
        result.append(row)

    return result

while True:
    if len(arr) == 1:
        break
    arr = pooling(arr)

print(arr[0][0])