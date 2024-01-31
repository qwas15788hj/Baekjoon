n = int(input())

answer = 5
for i in range(2, n+1):
    answer += i*3+1

print(answer%45678)