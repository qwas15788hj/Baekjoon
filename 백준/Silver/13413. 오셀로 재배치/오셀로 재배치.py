t = int(input())
for _ in range(t):
    n = int(input())
    begin = list(input())
    target = list(input())

    black, white = 0, 0
    for i in range(n):
        if begin[i] != target[i]:
            if target[i] == "B":
                black += 1
            else:
                white += 1

    answer = black + white - min(black, white)
    print(answer)