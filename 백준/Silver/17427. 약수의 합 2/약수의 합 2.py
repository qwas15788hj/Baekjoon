n = int(input())
answer = 0

for i in range(1, n+1):
    answer += (n//i)*i
print(answer)