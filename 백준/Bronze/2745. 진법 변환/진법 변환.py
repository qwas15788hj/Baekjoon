b, n = map(str, input().split())
b = b[::-1]
n = int(n)

answer = 0
for i in range(len(b)):
    x = 0
    if 65 <= ord(b[i]) <= 90:
        x = 10+ord(b[i])-65
    else:
        x = int(b[i])

    answer += (n**i) * x

print(answer)