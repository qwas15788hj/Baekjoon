n = int(input())
for i in range(n):
    num, s = input().split()
    result = ""
    for j in s:
        result += j*int(num)
    print(result)