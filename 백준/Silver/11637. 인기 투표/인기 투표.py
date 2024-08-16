t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(input()) for _ in range(n)]

    total = sum(arr)
    high = max(arr)

    if arr.count(high) > 1:
        print("no winner")
    else:
        if high > total//2:
            print("majority winner", arr.index(high)+1)
        else:
            print("minority winner", arr.index(high)+1)
