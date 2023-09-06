import sys
input = sys.stdin.readline

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

korean = a//c
if a%c != 0:
    korean += 1

math = b//d
if b%d != 0:
    math += 1

print(l - max(korean, math))