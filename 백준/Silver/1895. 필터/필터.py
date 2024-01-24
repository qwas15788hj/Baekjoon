r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
t = int(input())
result = []

for i in range(r-3+1):
    for j in range(c-3+1):
        check = []
        for k in range(3):
            for z in range(3):
                check.append(arr[i+k][j+z])
        check.sort()
        result.append(check[4])

answer = 0
for r in result:
    if r >= t:
        answer += 1

print(answer)