n = int(input())
arr = list(map(int, input().split()))
t, p = map(int, input().split())

a1 = 0
for i in range(len(arr)):
    a1 += arr[i]//t
    if arr[i]%t != 0:
        a1 += 1

print(a1)
print(n//p, n%p)