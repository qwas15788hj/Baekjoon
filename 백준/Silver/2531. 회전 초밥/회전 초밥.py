n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr += [arr[i] for i in range(k-1)]
arr = [0] + arr

answer = 0
dic = dict()
for i in range(k):
    if arr[i] in dic:
        dic[arr[i]] += 1
    else:
        dic[arr[i]] = 1

for i in range(n):
    if dic[arr[i]] == 1:
        del dic[arr[i]]
    else:
        dic[arr[i]] -= 1

    if arr[i+k] in dic:
        dic[arr[i+k]] += 1
    else:
        dic[arr[i+k]] = 1

    if c in dic:
        answer = max(answer, len(dic))
    else:
        answer = max(answer, len(dic)+1)

print(answer)