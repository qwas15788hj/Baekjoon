n = int(input())
arr = list(map(int, input().split()))

answer = 0
for i in range(4):
    num = 0
    check = 1
    if i !=3 :
        num = sum(arr[0:i]) + sum(arr[-3+i:])
        for j in arr[i:-3 + i]:
            check *= j
        num += check

    else:
        num = sum(arr[0:i])
        for j in arr[i:]:
            check *= j
        num += check

    answer = max(answer, num)

print(answer)