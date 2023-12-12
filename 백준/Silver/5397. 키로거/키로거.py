n = int(input())
for _ in range(n):
    left = []
    right = []
    s = input()
    for i in range(len(s)):
        if s[i] == "<":
            if left:
                right.append(left.pop())
        elif s[i] == ">":
            if right:
                left.append(right.pop())
        elif s[i] == "-":
            if left:
                left.pop()
        else:
            left.append(s[i])

    print("".join(left) + "".join(right[::-1]))