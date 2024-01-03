import sys
input = sys.stdin.readline

k, l = map(int, input().split())
dic = dict()
num = 0
for _ in range(l):
    std = input().strip()
    dic[std] = num
    num += 1

algo = sorted(dic.items(), key=lambda x:x[1])
for i in range(min(len(algo), k)):
    print(algo[i][0])