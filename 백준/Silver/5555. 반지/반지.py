word = input()
n = int(input())

answer = 0
for i in range(n):
    s = input()
    size = len(s)
    s += s[:len(word)-1]
    for j in range(size):
        if s[j:j+len(word)] == word:
            answer += 1
            break

print(answer)