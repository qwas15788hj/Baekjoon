from itertools import permutations

n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

for value in permutations(arr, n):
    flag = True
    weight = 500
    for v in value:
        weight += (v-k)
        if weight < 500:
            flag = False
            break

    if flag == True:
        count += 1

print(count)