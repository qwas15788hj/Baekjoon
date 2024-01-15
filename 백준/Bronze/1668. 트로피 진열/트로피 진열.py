n = int(input())
arr = [int(input()) for _ in range(n)]
left, right = 0, 0

height = 0
for i in range(n):
    if arr[i] > height:
        left += 1
        height = arr[i]

arr.reverse()
height = 0
for i in range(n):
    if arr[i] > height:
        right += 1
        height = arr[i]

print(left)
print(right)