arr = list(map(int, input().split()))
arr_sub = []
for i in range(4):
    arr.append(arr.pop(0))
    num = 0
    for j in range(4):
        num += arr[j] * (10**(3-j))
    arr_sub.append(num)

arr_sub.sort()
check = arr_sub[0]

store = set()
answer = 0
for i in range(1, 10):
    for j in range(1, 10):
        for z in range(1, 10):
            for k in range(1, 10):
                num_list = [i, j, z, k]
                num_list_sub = []
                for _ in range(4):
                    num_list.append(num_list.pop(0))
                    num = 0
                    for p in range(4):
                        num += num_list[p] * (10**(3-p))
                    num_list_sub.append(num)

                num_list_sub.sort()
                if num_list_sub[0] not in store and num_list_sub[0] < check:
                    store.add(num_list_sub[0])

print(len(store) + 1)