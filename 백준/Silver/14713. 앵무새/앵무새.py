import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
parrot = []
for i in range(n):
    parrot.append(deque(list(map(str, input().split()))))
arr = list(map(str, input().split()))

flag = True
for i in range(len(arr)):
    check = False
    for j in range(len(parrot)):
        if len(parrot[j]) == 0:
            continue
        if parrot[j][0] == arr[i]:
            parrot[j].popleft()
            break
    else:
        flag = False
        break

for i in range(len(parrot)):
    if len(parrot[i]) != 0:
        flag = False
        break

if flag:
    print("Possible")
else:
    print("Impossible")