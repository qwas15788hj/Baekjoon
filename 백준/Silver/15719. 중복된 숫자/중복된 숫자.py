import sys
input = sys.stdin.readline

n = int(input())
total = sum(range(1, int(n)))
arr = input().rstrip()
count = 0
temp = ""
for a in arr:
    if a.isdigit():
        temp += a
    else:
        count += int(temp)
        temp = ""

count += int(temp)

print(count - total)