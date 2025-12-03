n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    m = arr[i][0]
    soldier = arr[i][1:]
    dic = dict()
    for s in soldier:
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1

    for key, value in dic.items():
        if value > m//2:
            print(key)
            break
    else:
        print("SYJKGW")