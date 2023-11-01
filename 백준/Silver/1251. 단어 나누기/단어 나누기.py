s = list(input())
n = len(s)
arr = []

for i in range(1, n-1):
    for j in range(i+1, n):
        a = s[:i]
        b = s[i:j]
        c = s[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        arr.append(a + b + c)

arr.sort()
print("".join(arr[0]))