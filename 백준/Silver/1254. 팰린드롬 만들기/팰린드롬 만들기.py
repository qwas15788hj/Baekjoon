s = input()
rev_s = s[::-1][1:]

answer = 0
for i in range(len(rev_s)+1):
    word = s + rev_s[i:]
    if word == word[::-1]:
        answer = len(word)

print(answer)