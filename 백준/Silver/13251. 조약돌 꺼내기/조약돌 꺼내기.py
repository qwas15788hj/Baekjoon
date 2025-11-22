m = int(input())
arr = list(map(int, input().split()))
k = int(input())

total = 1
for i in range(k):
    total *= sum(arr) - i

check = 0
for i in range(m):
    c = 1
    for j in range(k):
        c *= arr[i] - j
    check += c

print(check/total)