w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

x += t
y += t
ax, ay = 0, 0
if (x//w)%2 == 0:
    ax = x%w
else:
    ax = w - (x%w)

if (y//h)%2 == 0:
    ay = y%h
else:
    ay = h - (y%h)

print(ax, ay)