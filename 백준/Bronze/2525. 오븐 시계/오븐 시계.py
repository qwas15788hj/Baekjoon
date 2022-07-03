h, m = map(int, input().split())
k = int(input())

if m+k >= 60:
    if h+(m+k)//60 >= 24:
        h = h+(m+k)//60 - 24
    else:
        h += (m+k)//60
    m = (m+k)%60
else:
    m += k
print(h, m)