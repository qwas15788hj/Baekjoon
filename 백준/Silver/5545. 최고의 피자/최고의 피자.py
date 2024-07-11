n = int(input())
a, b = map(int, input().split())
c = int(input())
d = [int(input()) for _ in range(n)]

d.sort(reverse=True)
money = a
cal = c
answer = cal//money
for i in range(n):
    money += b
    cal += d[i]
    if answer > cal//money:
        break
    answer = cal//money

print(answer)