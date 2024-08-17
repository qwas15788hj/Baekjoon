import sys
input = sys.stdin.readlines()

arr = []
for i in input:
    for j in i.split():
        arr.append(int(j[::-1]))

arr = arr[1:]
arr.sort()
for i in arr:
    print(i)