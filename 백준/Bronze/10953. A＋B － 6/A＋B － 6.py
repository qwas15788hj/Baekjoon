t = int(input())
arr = [list(input()) for _ in range(t)]

for i in range(t):
    print(int(arr[i][0]) + int(arr[i][-1]))