n = int(input())
target = 0
count = 0
i = 1
while target <= n:
    target += i
    i += 1
    count += 1
print(count-1)