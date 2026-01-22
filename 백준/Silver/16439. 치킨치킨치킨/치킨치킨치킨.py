from itertools import combinations

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

idx = [i for i in range(m)]
comb = list(combinations(idx, 3))

answer = 0
for x, y, z in comb:
    score = 0
    for i in range(n):
        score += max(arr[i][x], max(arr[i][y], arr[i][z]))
    answer = max(answer, score)

print(answer)