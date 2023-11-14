k = int(input())
a, b = [0] * (k+1), [0] * (k+1)
a[0] = 1

for i in range(1, k+1):
    a[i] = b[i-1]
    b[i] = a[i-1] + b[i-1]

print(a[-1], b[-1])