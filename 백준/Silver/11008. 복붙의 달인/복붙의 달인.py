t = int(input())
for _ in range(t):
    s, p = map(str, input().split())
    count = 0
    count = s.count(p)
    sub_s = s.replace(p, "")

    print(count + len(sub_s))