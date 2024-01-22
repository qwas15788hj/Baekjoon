arr = [list(map(int, input().split())) for _ in range(5)]

def check(n):
    for i in range(5):
        if n in arr[i]:
            idx = arr[i].index(n)
            arr[i][idx] = 0

def width():
    count = 0
    for i in range(5):
        if sum(arr[i]) == 0:
            count += 1

    return count

def length():
    count = 0
    for i in range(5):
        s = 0
        for j in range(5):
            s += arr[j][i]
        if s == 0:
            count += 1

    return count

def left():
    s = 0
    for i in range(5):
        s += arr[i][i]

    if s == 0:
        return 1
    else:
        return 0

def right():
    s = 0
    for i in range(5):
        s += arr[i][4-i]

    if s == 0:
        return 1
    else:
        return 0

command = [list(map(int, input().split())) for _ in range(5)]

flag = False
answer = 0
for com in command:
    for c in com:
        answer += 1
        check(c)
        if width() + length() + left() + right() >= 3:
            flag = True
            break

    if flag:
        break

print(answer)