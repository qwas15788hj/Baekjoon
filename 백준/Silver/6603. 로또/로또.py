from itertools import combinations

while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    if k == 0:
        break
    answer = list(combinations(sorted(arr[1:]), 6))
    for i in answer:
        print(*i)
    print()