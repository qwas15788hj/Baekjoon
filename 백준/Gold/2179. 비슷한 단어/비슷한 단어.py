import sys
input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]

max_prefix_length = 0
result = []

for i in range(n-1):
    for j in range(i+1, n):
        prefix_length = 0
        for k in range(min(len(arr[i]), len(arr[j]))):
            if arr[i][k] == arr[j][k]:
                prefix_length += 1
            else:
                break
        if prefix_length > max_prefix_length:
            max_prefix_length = prefix_length
            result = [arr[i], arr[j]]

print(result[0])
print(result[1])
