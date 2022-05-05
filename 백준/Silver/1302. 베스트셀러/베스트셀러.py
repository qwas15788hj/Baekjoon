from collections import Counter

n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

answer = Counter(arr).most_common()
answer.sort(key=lambda x:(-x[1], x[0]))
print(answer[0][0])