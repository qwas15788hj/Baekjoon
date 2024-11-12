import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
queue = deque(["?"] * n)
flag = True

for i in range(k):
    count, s = map(str, input().split())
    count = int(count)

    if i == 0:
        queue[0] = s
    else:
        for j in range(count):
            queue.appendleft(queue.pop())

        if queue[0] != "?" and queue[0] != s:
            flag = False
            break

        queue[0] = s

dic = dict()
for i in range(len(queue)):
    if queue[i] != "?":
        if queue[i] in dic:
            flag = False
            break
        dic[queue[i]] = 1

if flag:
    answer = ""
    for i in range(len(queue)):
        answer += queue[i]
    print(answer)
else:
    print("!")