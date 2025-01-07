import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(m):
    k = int(input())
    a = list(map(int, input().split()))
    arr.append(a)

flag = True
for i in range(len(arr)):
    for j in range(len(arr[i])-1):
        if arr[i][j] < arr[i][j+1]:
            flag = False
            break

    if not flag:
        break

if flag:
    print("Yes")
else:
    print("No")