import sys
input = sys.stdin.readline

n, m = map(int, input().split())
word = dict()
for _ in range(n):
    s = input().rstrip()
    if len(s) >= m:
        if s in word:
            word[s] += 1
        else:
            word[s] = 1

answer = []
for k, v in word.items():
    answer.append([k, v, len(k)])

answer.sort(key=lambda x:(-x[1], -x[2], x[0]))
for a in answer:
    print(a[0])