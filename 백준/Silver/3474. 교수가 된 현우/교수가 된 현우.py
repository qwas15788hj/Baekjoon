t = int(input())
for _ in range(t):
    n = int(input())
    answer = 0
    i = 5
    while i <= n:
        answer += n // i
        i *= 5

    print(answer)