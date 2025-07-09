import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [float(input()) for _ in range(n)]

arr.sort()
if k == 0:
    score_list = arr[:]
else:
    score_list = arr[k:-k]
score = sum(score_list) + 0.0000001
result = str(round(score/(n-2*k), 2))
if result[-2] == ".":
    result += "0"
print(result)

score_list += [score_list[0]]*k
score_list += [score_list[-(k+1)]]*k
score = sum(score_list) + 0.0000001
result = str(round(score/n, 2))
if result[-2] == ".":
    result += "0"
print(result)