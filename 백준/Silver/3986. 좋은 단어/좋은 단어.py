n = int(input())
answer = 0
for _ in range(n):
    s = input()
    arr = []

    for i in range(len(s)):
        if arr and arr[-1] == s[i]:
            arr.pop()
        else:
            arr.append(s[i])

    if not arr:
        answer += 1

print(answer)