n = int(input())
arr = [input() for _ in range(n)]

alpha = [0] * 26
for i in range(n):
    alpha[ord(arr[i][0])-97] += 1

answer = ""
for i in range(26):
    if alpha[i] >= 5:
        answer += chr(i+97)

if answer == "":
    print("PREDAJA")
else:
    print(answer)