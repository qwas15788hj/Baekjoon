n = int(input())

arr = [0] * (abs(n)+1)
if n != 0:
    arr[1] = 1
for i in range(2, abs(n)+1):
    arr[i] = (arr[i-2] + arr[i-1])%1000000000

if n < 0:
    if abs(n)%2 != 0:
        print(1)
    else:
        print(-1)
elif n == 0:
    print(0)
else:
    print(1)

print(arr[abs(n)]%1000000000)