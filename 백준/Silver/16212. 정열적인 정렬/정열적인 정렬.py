n = int(input())
arr = list(map(int, input().split()))
arr.sort()
for a in arr:
    print(a, end=" ")