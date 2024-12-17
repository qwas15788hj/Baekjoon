import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

houses = []
chicken = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            houses.append([i, j])
        if arr[i][j] == 2:
            chicken.append([i, j])

chicken_comb = list(combinations(chicken, m))
answer = 1e9
for combs in chicken_comb:
    distance = 0
    for house in houses:
        dist = 1e9
        for comb in combs:
            dist = min(dist, abs(house[0]-comb[0]) + abs(house[1]-comb[1]))
        distance += dist

    answer = min(answer, distance)

print(answer)