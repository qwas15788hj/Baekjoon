n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dic = dict()
dic[0] = 5
dic[1] = 3
dic[2] = 4
dic[3] = 1
dic[4] = 2
dic[5] = 0

answer = 0
# 6번
for i in range(6):
    result = 0
    idx = i
    for k in range(6):
        if k != idx and k != dic[idx]:
            result = max(result, arr[0][k])
    idx = arr[1].index(arr[0][dic[idx]])
    for j in range(1, n-1):
        num = 0
        for k in range(6):
            if k != idx and k != dic[idx]:
                num = max(num, arr[j][k])
        result += num
        idx = arr[j+1].index(arr[j][dic[idx]])

    num = 0
    for k in range(6):
        if k != idx and k != dic[idx]:
            num = max(num, arr[-1][k])
    result += num

    answer = max(answer, result)

print(answer)