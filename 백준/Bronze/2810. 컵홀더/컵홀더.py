n = int(input())
s = input()
count = 0
for i in s:
    if i == "L":
        count += 1

count //= 2

print(min(n, n-count+1))