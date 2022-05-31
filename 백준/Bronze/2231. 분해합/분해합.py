n = int(input())

def divsum(n):
    m = n
    for i in str(n):
        m += int(i)
    return m

num = 0
while True:
    m = divsum(num)
    if n == m:
        answer = num
        break
    if num > n:
        answer = 0
        break
    num += 1
print(answer)