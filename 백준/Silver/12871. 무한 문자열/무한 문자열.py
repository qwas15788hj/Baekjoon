s = input()
t = input()

def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

n = len(s)
m = len(t)
if s * (lcm(n, m)//n) == t * (lcm(n, m)//m):
    print(1)
else:
    print(0)