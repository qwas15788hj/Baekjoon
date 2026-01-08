n = int(input())
word = input()
score = list(map(int, input().split()))

s = "UOSPC"
arr = [[0] * n for _ in range(5)]

for i in range(n):
    if word[i] == s[0]:
        arr[0][i] = score[i]

for i in range(1, 5):
    check = 10**18
    for j in range(n):
        if word[j] == s[i] and check != 10**18:
            arr[i][j] = check + score[j]
        if arr[i-1][j] != 0:
            check = min(check, arr[i-1][j])

answer = 10**18
for a in arr[-1]:
    if a != 0:
        answer = min(answer, a)

if answer == 10**18:
    print(-1)
else:
    print(answer)