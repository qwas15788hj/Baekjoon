h, y = map(int, input().split())

arr = [0] * (y+1)
arr[0] = h
for i in range(1, y+1):
    arr[i] = max(arr[i], arr[i-1] + arr[i-1]*5//100)

    if i >= 3:
        arr[i] = max(arr[i], arr[i-3] + arr[i-3]*20//100)

    if i >= 5:
        arr[i] = max(arr[i], arr[i-5] + arr[i-5]*35//100)

print(arr[-1])