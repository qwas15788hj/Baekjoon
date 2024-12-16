n = int(input())

def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y / gcd(x, y)

for _ in range(n):
    a, b = map(int, input().split())
    print(int(lcm(a, b)))
