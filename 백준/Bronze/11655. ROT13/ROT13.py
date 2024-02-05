answer = ""
s = input()
for i in range(len(s)):
    if s[i].isalpha():
        check = ord(s[i])
        if ord("a") <= check <= ord("m"):
            answer += chr(check+13)
        elif ord("m") < check <= ord("z"):
            answer += chr(check-13)
        elif ord("A") <= check <= ord("M"):
            answer += chr(check+13)
        elif ord("M") < check <= ord("Z"):
            answer += chr(check-13)
    else:
        answer += s[i]

print(answer)