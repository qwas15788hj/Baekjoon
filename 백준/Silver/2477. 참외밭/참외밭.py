k = int(input())

arr = []
x, y = [], []
low = []
for i in range(6):
    a, b = map(int, input().split())
    arr.append([a, b])
    if arr[i][0] == 3 or arr[i][0] == 4:
        x.append(b)
    else:
        y.append(b)

for i in range(6):
    if arr[i][0] == arr[(i+2)%6][0]:
        low.append(arr[(i+1)%6][1])

print((max(x)*max(y) - low[0]*low[1]) * k)