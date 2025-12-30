from itertools import combinations

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append([i, j])
        if arr[i][j] == 2:
            chicken.append([i, j])

answer = 1e9
for comb in list(combinations(chicken, m)):
    result = 0
    for h in house:
        check = 1e9
        for c in comb:
            check = min(check, abs(h[0]-c[0])+abs(h[1]-c[1]))
        result += check
    answer = min(answer, result)

print(answer)