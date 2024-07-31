import sys
input = sys.stdin.readline

dic = dict()
total = 0
while True:
    s = input().rstrip()
    if s == "":
        break
    else:
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1
        total += 1

sdic = dict(sorted(dic.items()))
for i in sdic:
    rate = sdic[i] / total * 100
    print("%s %.4f" %(i, rate))