n = int(input())
dic = dict()
for i in range(n):
    s = input()
    dic[s] = i

answer = 0
arr = [input() for _ in range(n)]
for i in range(n-1):
    for j in range(i+1, n):
        if dic[arr[i]] > dic[arr[j]]:
            answer += 1
            break

print(answer)