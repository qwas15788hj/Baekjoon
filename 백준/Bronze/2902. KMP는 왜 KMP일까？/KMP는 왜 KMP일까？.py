s = input()

answer = s[0]
for i in range(len(s)):
    if s[i] == "-":
        answer += s[i+1]

print(answer)