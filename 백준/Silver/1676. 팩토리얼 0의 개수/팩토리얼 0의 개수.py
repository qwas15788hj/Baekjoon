import math

n = int(input())
a = str(math.factorial(n))[::-1]
answer = 0

for i in a:
    if i == '0':
        answer += 1
    else:
        break
        
print(answer)