from itertools import permutations

a, b = map(int, input().split())
arr = [i for i in range(len(str(a)))]

answer = -1
for per in list(permutations(arr, len(arr))):
    check = ""
    for p in per:
        check += str(a)[p]

    if check[0] != "0":
        if int(check) < b:
            answer = max(answer, int(check))

print(answer)