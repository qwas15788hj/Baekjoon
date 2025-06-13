d, k = map(int, input().split())

arr = [[1, 0], [0, 1]]
for i in range(2, d):
    arr.append([arr[i-2][0]+arr[i-1][0], arr[i-2][1]+arr[i-1][1]])

a, b = arr[-1][0], arr[-1][1]
for i in range(k//b, 0, -1):
    y = i
    x = (k-(y*b))
    if x//a > 0 and y > 0 and y > x//a and x%a == 0:
        print(x//a)
        print(y)
        break