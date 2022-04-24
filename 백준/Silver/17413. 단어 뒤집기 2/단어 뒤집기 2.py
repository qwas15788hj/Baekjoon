s = input()
flag = False
stack = ""
answer = ""

for i in s:
    if flag == False:
        if i == "<":
            stack += i
            flag = True
        elif i == " ":
            stack += i
            answer += stack
            stack = ""
        else:
            stack = i + stack
    else:
        stack += i
        if i == ">":
            answer += stack
            flag = False
            stack = ""
print(answer+stack)