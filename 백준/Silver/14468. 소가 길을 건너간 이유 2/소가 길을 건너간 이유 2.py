s = input()
arr = []
check = [False] * 26
answer = 0

for i in range(len(s)):
    if check[ord(s[i]) - 65]:
        idx = arr.index(s[i])
        answer += len(arr) - (idx + 1)
        arr.pop(idx)
    else:
        arr.append(s[i])
        check[ord(s[i]) - 65] = True

print(answer)