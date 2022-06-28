n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

m, k = map(int, input().split())
b = []
for _ in range(m):
    b.append(list(map(int, input().split())))

answer = []
for i in range(n):
    arr = []
    for j in range(k):
        num = 0
        for z in range(m):
            num += a[i][z]*b[z][j]
        arr.append(num)
    answer.append(arr)

for i in answer:
    for j in i:
        print(j, end=" ")
    print()