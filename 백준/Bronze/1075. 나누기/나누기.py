n = int(input())
f = int(input())

n = int(str(n)[:-2] + "00")
for i in range(100):
    num = (n+i)
    if num%f == 0:
        print(str(num)[-2:])
        break