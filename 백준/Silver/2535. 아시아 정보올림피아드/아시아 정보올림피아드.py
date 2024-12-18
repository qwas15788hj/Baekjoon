import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:-x[2])

dic = dict()
answer = []
for i in range(n):
    if arr[i][0] not in dic:
        dic[arr[i][0]] = 1
        answer.append([arr[i][0], arr[i][1]])
    elif dic[arr[i][0]] == 1:
        dic[arr[i][0]] += 1
        answer.append([arr[i][0], arr[i][1]])

    if len(answer) == 3:
        break

for i in range(len(answer)):
    print(answer[i][0], answer[i][1])