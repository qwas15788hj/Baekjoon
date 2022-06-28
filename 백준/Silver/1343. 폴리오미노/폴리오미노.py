s = input()

answer = ""
count = 0
flag = True
for i in range(len(s)):
    if s[i] == "X":
        count += 1
    if s[i] == ".":
        if count%2 != 0:
            flag = False
            break
        else:
            answer += "AAAA"*(count//4)
            count %= 4
            answer += "BB"*(count//2)
            count = 0
            answer += "."
    if s[i] == "X" and i+1 == len(s):
        if count%2 != 0:
            flag = False
            break
        else:
            answer += "AAAA"*(count//4)
            count %= 4
            answer += "BB"*(count//2)
            count = 0

if flag == True:
    print(answer)
else:
    print(-1)