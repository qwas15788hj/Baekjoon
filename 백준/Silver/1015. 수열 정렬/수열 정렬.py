n = int(input())
arr = list(map(int, input().split()))
sub = [[0]*3 for i in range(n)]

for i in range(n):
    sub[i][0], sub[i][1] = arr[i], i
sub.sort(key=lambda x:(x[0], x[1]))

for i in range(n):
    sub[i][2] = i
sub.sort(key=lambda x:x[1])

for i in range(n):
    print(sub[i][2], end=" ")