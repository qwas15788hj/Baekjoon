s = input()

answer = 0
if s[0] == "c":
    answer = 26
else:
    answer = 10

for i in range(1, len(s)):
    if s[i] == "c":
        if s[i-1] == s[i]:
            answer *= 25
        else:
            answer *= 26
    else:
        if s[i-1] == s[i]:
            answer *= 9
        else:
            answer *= 10

print(answer)