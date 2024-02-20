n = int(input())
for _ in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    arr = []
    for i in range(4, 0, -1):
        if a[1:].count(i) > b[1:].count(i):
            arr.append("A")
        elif a[1:].count(i) < b[1:].count(i):
            arr.append("B")
        else:
            arr.append("D")

    for i in range(len(arr)):
        if arr[i] != "D":
            print(arr[i])
            break
    else:
        print("D")