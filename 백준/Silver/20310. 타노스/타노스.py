s = list(input())
zero, one = s.count("0")//2, s.count("1")//2

for _ in range(zero):
    s.pop(-s[::-1].index("0")-1)
for _ in range(one):
    s.pop(s.index("1"))

print("".join(s))