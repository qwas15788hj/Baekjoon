num = ["2", "3", "4", "5", "6", "7", "8", "9"]
alpha = ["H", "C", "O"]
count = [0, 0, 0]

arr = list(input())
for i in range(len(arr)):
    if arr[i] in num and (arr[i-1] != '(' and arr[i-1] != ')'):
        arr[i] = arr[i-1] * (int(arr[i])-1)

stack = []
now = ""
for i in range(len(arr)):
    if arr[i] == ")":
        while True:
            s = stack.pop()
            if s == "(":
                break
            else:
                now += s
    else:
        if arr[i] in num:
            stack.append(now * (num.index(arr[i])+2))
        else:
            if now != "":
                stack.append(now)
            stack.append(arr[i])
        now = ""

answer = 0
for i in range(len(stack)):
    for j in range(len(stack[i])):
        if stack[i][j] == "H":
            answer += 1
        elif stack[i][j] == "C":
            answer += 12
        else:
            answer += 16
for i in range(len(now)):
    if now[i] == "H":
        answer += 1
    elif now[i] == "C":
        answer += 12
    else:
        answer += 16

print(answer)