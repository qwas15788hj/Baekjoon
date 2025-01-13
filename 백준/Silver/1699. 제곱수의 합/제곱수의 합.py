import sys
input = sys.stdin.readline

n = int(input())
arr = [1e9] * (n+1)
arr[1] = 1
num = []
for i in range(2, n+1):
    arr[i] = i
    if i**0.5 == int(i**0.5):
        arr[i] = 1
        num.append(i)
    else:
        for j in num:
            arr[i] = min(arr[i], arr[j] + arr[i-j])

print(arr[n])