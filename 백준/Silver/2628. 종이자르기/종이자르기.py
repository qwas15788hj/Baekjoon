n, m = map(int, input().split())
width, length = [0, n], [0, m]
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a == 0:
        length.append(b)
    else:
        width.append(b)

width.sort()
length.sort()
answer = 0
for i in range(1, len(width)):
    for j in range(1, len(length)):
        answer = max(answer, (width[i] - width[i-1]) * (length[j] - length[j-1]))

print(answer)