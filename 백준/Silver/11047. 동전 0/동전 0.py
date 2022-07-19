a, b = map(int, input().split())
coin = []
for i in range(a):
    c = int(input())
    coin.append(c)
coin.sort(reverse=True)

count = 0
for i in coin:
    count += b//i
    b %= i
print(count)