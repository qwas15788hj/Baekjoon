from itertools import combinations

n = int(input())

a = [i for i in range(9, -1, -1)]
arr = []
for i in range(1, 11):
    comb = list(combinations(a, i))
    comb = [''.join(map(str, x)) for x in comb]
    for com in comb:
        if len(com) > 1 and com[0] == "0":
            continue
        arr.append(int(com))

arr = list(set(arr))
arr.sort()

if n-1 >= len(arr):
    print(-1)
else:
    print(arr[n-1])