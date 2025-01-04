n = int(input())
arr = list(map(int, input().split()))
num = [0] * (max(arr) + 1)
for i in range(n):
    num[arr[i]] += 1

flag = False
answer = 0
for i in range(len(num)-1, -1, -1):
    if i == num[i]:
        answer = i
        flag = True
        break

if flag:
    print(answer)
else:
    print(-1)