a = input()
b = input()
n = 0
answer = 0

while n <= len(a) - len(b):
    if a[n:n+len(b)] == b:
        n += len(b)
        answer += 1
    else:
        n += 1
print(answer)