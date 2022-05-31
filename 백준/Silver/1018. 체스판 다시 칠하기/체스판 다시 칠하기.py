n, m = map(int, input().split())

def board_check(x, y):
    count = 0
    for i in range(x, x+8):
        for j in range(y, y+8):
            if i == x and j == y:
                continue
            if (x+y)%2 == 0:
                if (i+j)%2 == 0 and arr[i][j] != arr[x][y]:
                    count += 1
                if (i+j)%2 != 0 and arr[i][j] == arr[x][y]:
                    count += 1
            if (x+y)%2 != 0:
                if (i+j)%2 != 0 and arr[i][j] != arr[x][y]:
                    count += 1
                if (i+j)%2 == 0 and arr[i][j] == arr[x][y]:
                    count += 1
    return count

arr = []
for _ in range(n):
    arr.append(list(input()))

answer = 1e9
for i in range(n-8+1):
    for j in range(m-8+1):
        result = board_check(i, j)
        answer = min(answer, result, 64-result)

print(answer)