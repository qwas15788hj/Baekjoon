n = int(input())
arr = list(input())
alpha = [0] * 26
for i in range(n):
    alpha[i] = int(input())

stack = []
for i in range(len(arr)):
    if arr[i].isalpha():
        stack.append(alpha[ord(arr[i])-65])
    else:
        b = stack.pop()
        a = stack.pop()
        if arr[i] == "+":
            stack.append(a+b)
        elif arr[i] == "-":
            stack.append(a-b)
        elif arr[i] == "*":
            stack.append(a*b)
        else:
            stack.append(a/b)

print("{:.2f}".format(stack[0]))