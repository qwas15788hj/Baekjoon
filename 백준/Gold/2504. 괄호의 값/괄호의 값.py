s = input()

# 올바른 괄호인지 체크
arr = []
flag = True
for i in range(len(s)):
    if s[i] == "(" or s[i] == "[":
        arr.append(s[i])
    elif s[i] == ")":
        if len(arr) != 0 and arr[-1] == "(":
            arr.pop()
        else:
            flag = False
            break
    elif s[i] == "]":
        if len(arr) != 0 and arr[-1] == "[":
            arr.pop()
        else:
            flag = False
            break

if len(arr) != 0:
    flag = False

# 올바른 괄호면 값 구하기
if flag:
    arr = []
    for i in range(len(s)):
        if s[i] == "(" or s[i] == "[":
            arr.append(s[i])
        elif s[i] == ")":
            count = 0
            while True:
                p = arr.pop()
                if p == "(":
                    if count == 0:
                        arr.append(2)
                    else:
                        arr.append(count * 2)
                    break
                else:
                    count += p
        elif s[i] == "]":
            count = 0
            while True:
                p = arr.pop()
                if p == "[":
                    if count == 0:
                        arr.append(3)
                    else:
                        arr.append(count * 3)
                    break
                else:
                    count += p

    print(sum(arr))
else:
    print(0)