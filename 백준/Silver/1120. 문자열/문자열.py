x, y = map(str, input().split())
n, m = len(x), len(y)

answer = 1e9
for i in range(m-n+1):
    s = y[i:i+n]
    count = 0
    for j in range(n):
        if x[j] != s[j]:
            count += 1
    answer = min(answer, count)

print(answer)