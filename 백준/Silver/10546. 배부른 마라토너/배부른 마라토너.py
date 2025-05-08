import sys
input = sys.stdin.readline

n = int(input())
dic = dict()
for _ in range(n):
    s = input()
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1

for _ in range(n-1):
    s = input()
    dic[s] -= 1

for key, values in dic.items():
    if values == 1:
        print(key)
        break