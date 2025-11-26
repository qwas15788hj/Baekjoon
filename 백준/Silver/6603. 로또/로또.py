from itertools import combinations

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break

    n = arr[0]
    comb = list(combinations(arr[1:], 6))
    for com in comb:
        print(*com)
    print()