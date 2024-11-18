s = input()
answer = s
for i in range(1, len(s)):
    for j in range(i+1, len(s)):
        answer = min(answer, s[:i][::-1] + s[i:j][::-1] + s[j:][::-1])

print(answer)