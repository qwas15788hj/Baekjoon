t = int(input())

def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)
    
def lcm(x, y):
    return x*y // gcd(x, y)

for _ in range(t):
    a, b = map(int, input().split())
    print(lcm(a, b))