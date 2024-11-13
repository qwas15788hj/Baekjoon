n, m = map(int, input().split())
a, b = map(str, input().split())
count = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
arr = []
for i in range(min(n, m)):
    arr.append(count[ord(a[i])-65])
    arr.append(count[ord(b[i])-65])

if len(a) > min(n, m):
    for i in range(min(n, m), max(n, m)):
        arr.append(count[ord(a[i])-65])
if len(b) > min(n, m):
    for i in range(min(n, m), max(n, m)):
        arr.append(count[ord(b[i])-65])

while True:
    if len(arr) == 2:
        break
    for i in range(len(arr)-1):
        arr[i] = (arr[i] + arr[i+1])%10
    arr.pop()

print(str(int(arr[0])*10 + int(arr[1])) + "%")