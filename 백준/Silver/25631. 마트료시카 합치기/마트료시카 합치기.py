n = int(input())
arr = list(map(int, input().split()))

answer = 0
while True:
    remove = []
    sub_arr = []
    for i in range(len(arr)):
        if arr[i] not in remove:
            remove.append(arr[i])
        else:
            sub_arr.append(arr[i])

    if len(remove) == 0:
        break

    arr = sub_arr
    answer += 1

print(answer)