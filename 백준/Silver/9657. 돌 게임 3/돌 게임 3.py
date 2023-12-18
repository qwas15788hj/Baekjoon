n = int(input())
arr = [0] * 1001
arr[2] = 1

for i in range(5, n+1):
    if arr[i-1] == 0 and arr[i-3] == 0 and arr[i-4] == 0:
        arr[i] = 1
    else:
        arr[i] = 0

if arr[n] == 0:
    print("SK")
else:
    print("CY")