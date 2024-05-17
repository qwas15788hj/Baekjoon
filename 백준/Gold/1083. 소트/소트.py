n = int(input())
arr = list(map(int, input().split()))
s = int(input())

for i in range(n-1):
    if s != 0:
        count = min(len(arr[i+1:]), s)
        num = max(arr[i+1:i+1+count])
        if arr[i] < num:
            idx = arr.index(num)
            arr.insert(i, arr.pop(idx))
            s -= (idx-i)
    else:
        break

print(*arr)