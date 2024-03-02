n = int(input())
answer = []
for _ in range(n):
    words = input()
    s = ""
    for word in words:
        if 97 <= ord(word) <= 122:
            if len(s) > 0:
                answer.append(s)
            s = ""
        else:
            s += word

    if len(s) > 0:
        flag = True
        for i in range(len(s)):
            if 97 <= ord(s[i]) <= 122:
                flag = False
                break

        if flag:
            answer.append(s)

for i in range(len(answer)):
    answer[i] = int(answer[i])
answer.sort()

for a in answer:
    print(a)