r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

answer = []
for i in range(r):
    s = ""
    for j in range(c):
        if arr[i][j] == "#":
            if len(s) > 1:
                answer.append(s)
            s = ""
        else:
            s += arr[i][j]
    if len(s) > 1:
        answer.append(s)

for i in range(c):
    s = ""
    for j in range(r):
        if arr[j][i] == "#":
            if len(s) > 1:
                answer.append(s)
            s = ""
        else:
            s += arr[j][i]
    if len(s) > 1:
        answer.append(s)

answer.sort()
print(answer[0])
