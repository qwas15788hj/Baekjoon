x, y = map(int, input().split())

x = int(str(x)[::-1])
y = int(str(y)[::-1])
print(int(str(x+y)[::-1]))