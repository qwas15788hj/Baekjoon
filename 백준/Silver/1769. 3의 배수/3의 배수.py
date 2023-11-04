n = int(input())
count = 0

while len(str(n)) > 1:
    num = 0
    n = str(n)
    for i in range(len(n)):
        num += int(n[i])
    n = num
    count += 1

print(count)
if n % 3 == 0:
    print("YES")
else:
    print("NO")