import sys
input = sys.stdin.readline

arr = []
num = 1

while len(arr) < 1000000:
    flag = True
    visited = [False] * 10
    s = str(num)
    for i in range(len(s)):
        if visited[int(s[i])]:
            flag = False
            break
        else:
            visited[int(s[i])] = True

    if flag:
        arr.append(num)

    num += 1

while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(arr[n-1])