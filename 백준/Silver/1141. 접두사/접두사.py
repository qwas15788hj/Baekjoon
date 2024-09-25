n = int(input())
arr = [input() for _ in range(n)]
arr.sort(key=lambda x:-len(x))

dic = dict()
answer = 0
for i in range(n):
    if arr[i] not in dic:
        for j in range(len(arr[i])):
            dic[arr[i][:j+1]] = 1
        answer += 1

print(answer)