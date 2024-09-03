n = int(input())
arr = [input() for _ in range(n)]

answer = 0
for i in range(n-1):
    for j in range(i+1, n):
        dic1 = dict()
        dic2 = dict()
        flag = True
        for k in range(len(arr[i])):
            if arr[i][k] not in dic1:
                dic1[arr[i][k]] = arr[j][k]
            else:
                if dic1[arr[i][k]] != arr[j][k]:
                    flag = False
                    break
            if arr[j][k] not in dic2:
                dic2[arr[j][k]] = arr[i][k]
            else:
                if dic2[arr[j][k]] != arr[i][k]:
                    flag = False
                    break

            if not flag:
                break

        if flag:
            answer += 1

print(answer)