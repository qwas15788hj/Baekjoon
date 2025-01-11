import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))
a, b = dict(), dict()
for i in a_arr:
    a[i] = 1
for i in b_arr:
    b[i] = 1

for i in range(m):
    if b_arr[i] in a:
        del a[b_arr[i]]

answer = []
for key in a:
    answer.append(key)
answer.sort()

print(len(answer))
print(*answer)