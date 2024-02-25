h, w, n, m = map(int, input().split())
x = 1 + (h-1)//(n+1)
y = 1 + (w-1)//(m+1)
print(x*y)