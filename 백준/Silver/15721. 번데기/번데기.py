import sys
input = sys.stdin.readline

a = int(input())
t = int(input())
target = int(input())

arr = [0, 1, 0, 1, 0, 0, 1, 1]
pidx = 0
aidx = 0

answer = 0
while True:
    if arr[aidx] == target:
        answer += 1

    if answer == t:
        print(pidx)
        break

    pidx = (pidx + 1)%a
    aidx += 1
    if aidx == len(arr):
        arr.insert(4, 0)
        arr.append(1)
        aidx = 0