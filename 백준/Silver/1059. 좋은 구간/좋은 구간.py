l = int(input())
arr = list(map(int, input().split()))
n = int(input())

if n in arr:
    print(0)
else:
    answer = 0
    arr.append(n)
    arr.sort()
    idx = arr.index(n)

    start, end = 0, 0
    if idx == 0:
        start = 1
    else:
        start = arr[idx-1] + 1

    end = arr[idx+1]

    check = [i for i in range(start, end)]
    check_idx = check.index(n)
    answer += check_idx * (len(check) - check_idx)
    answer += len(check) - (check_idx + 1)

    print(answer)