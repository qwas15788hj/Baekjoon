n = int(input())
arr = list(map(int, input().split()))

answer = 0
result = 0
dic = dict()
for a in arr:
    if a not in dic:
        dic[a] = 0
        result += 1
        if result > answer:
            answer = result
    else:
        result -= 1

print(answer)