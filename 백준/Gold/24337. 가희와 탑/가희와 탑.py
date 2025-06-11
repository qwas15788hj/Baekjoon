import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())

if 1 <= b <= n-a+1:
    arr1 = [i for i in range(1, a)]
    arr2 = [i for i in range(b-1, 0, -1)]
    arr = arr1 + [max(a, b)] + arr2

    if len(arr1) == 0:
        for _ in range(n-len(arr)):
            arr.insert(1, 1)
    else:
        for _ in range(n-len(arr)):
            arr.insert(0, arr[0])

    print(*arr)
    
else:
    print(-1)