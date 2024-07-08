s = input()
answer = 0
stack = []

for i in range(len(s)):
    if s[i] == "(":
        stack.append(s[i])
    else:
        if stack:
            stack.pop()
        else:
            answer += 1

print(answer + len(stack))