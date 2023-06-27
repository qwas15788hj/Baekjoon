n = int(input())
m = int(input())
if m == 0:
    arr = []
else:
    arr = list(map(int, input().split()))

answer = abs(100-n)
for channel in range(999999):
    flag = True
    for ch in str(channel):
        if int(ch) in arr:
            flag = False
            break
    if flag:
        answer = min(answer, len(str(channel)) + abs(channel-n))

print(answer)