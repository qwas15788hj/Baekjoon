from collections import Counter

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(input())

answer = ""
count = 0
for i in range(m):
    dna = []
    for j in range(n):
        dna.append(arr[j][i])
    val = Counter(dna).most_common()
    val.sort(key=lambda x:(-x[1], x[0]))
    answer += val[0][0]
    count += n-val[0][1]

print(answer)
print(count)