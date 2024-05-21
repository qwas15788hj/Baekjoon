n = int(input())
arr = list(map(int, input().split()))

arrow = [0] * 1000001
for i in range(n):
    if arrow[arr[i]] > 0:
        arrow[arr[i]] -= 1
        arrow[arr[i]-1] += 1
    else:
        arrow[arr[i]-1] += 1

print(sum(arrow))