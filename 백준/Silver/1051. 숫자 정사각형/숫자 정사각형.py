n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

answer = 1
if m >= n:
    for i in range(1, n):
        for j in range(m-i):
            for z in range(n-i):
                if arr[z][j] == arr[z+i][j] and arr[z][j] == arr[z][j+i] and arr[z][j] == arr[z+i][j+i]:
                    answer = (i+1)**2

else:
    for i in range(1, m):
        for j in range(n-i):
            for z in range(m-i):
                if arr[j][z] == arr[j+i][z] and arr[j][z] == arr[j][z+i] and arr[j][z] == arr[j+i][z+i]:
                    answer = (i+1)**2

print(answer)