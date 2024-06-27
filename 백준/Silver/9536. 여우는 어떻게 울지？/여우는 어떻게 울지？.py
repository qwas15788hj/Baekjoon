t = int(input())
for _ in range(t):
    arr = list(map(str, input().split()))
    dic = dict()
    while True:
        animal = list(map(str, input().split()))
        if animal[-1] == "say?":
            break
        else:
            dic[animal[2]] = 1

    result = []
    for i in range(len(arr)):
        if arr[i] not in dic:
            result.append(arr[i])

    print(*result)