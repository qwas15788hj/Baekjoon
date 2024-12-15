s = input()
idx = s.index(":")
n = int(s[:idx])
m = int(s[idx+1:])

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

div = gcd(n, m)

print(f'{n//div}:{m//div}')