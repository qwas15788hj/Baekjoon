import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [input().strip() for _ in range(n)]

    for i in range(n):
        num = arr[i].replace(" ", "")
        arr[i] = num
    arr.sort(key=lambda x:len(x))

    dic = dict()
    dic[arr[0]] = 1
    flag = True
    for i in range(1, n):
        num = ""
        for j in range(len(arr[i])):
            num += arr[i][j]
            if num in dic:
                flag = False
                break

        dic[arr[i]] = 1

    if flag:
        print("YES")
    else:
        print("NO")