import math

a, b = map(int, input().split())
c, d = map(int, input().split())
lcm = (b*d) // math.gcd(b, d)

n, m = a*(lcm//b) + c*(lcm//d), lcm
gcd = math.gcd(n, m)

while gcd != 1:
    n //= gcd
    m //= gcd
    gcd = math.gcd(n, m)

print(n, m)