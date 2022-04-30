n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
start = arr[0]
end = arr[0]+l
count = 1

for i in range(n):
    if arr[i] >= start and arr[i] < end:
        continue
    else:
        start = arr[i]
        end = arr[i]+l
        count += 1
print(count)