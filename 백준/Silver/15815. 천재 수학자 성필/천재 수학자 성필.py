s = input()
arr = []
op = ["+", "-", "*", "/"]
for i in range(len(s)):
    if s[i] in op:
        num2 = arr.pop()
        num1 = arr.pop()
        if s[i] == "+":
            num1 += num2
        elif s[i] == "-":
            num1 -= num2
        elif s[i] == "*":
            num1 *= num2
        else:
            num1 //= num2
        arr.append(num1)
    else:
        arr.append(int(s[i]))

print(arr[0])