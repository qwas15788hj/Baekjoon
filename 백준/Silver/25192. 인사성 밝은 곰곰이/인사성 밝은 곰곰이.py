n = int(input())
answer = 0
dic = dict()
for _ in range(n):
    s = input()
    if s == "ENTER":
        dic = dict()
    else:
        if s not in dic:
            dic[s] = 1
            answer += 1

print(answer)