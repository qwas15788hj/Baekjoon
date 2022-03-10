import sys

n = int(sys.stdin.readline())
dic = {}

for _ in range(n):
    card = int(sys.stdin.readline())
    if card in dic:
        dic[card] += 1
    else:
        dic[card] = 1

result = sorted(dic.items(), key=lambda x:(-x[1], x[0]))
print(result[0][0])