n = int(input())
arr = [0, 0]
for _ in range(n):
    arr[int(input())] += 1

if arr[0] > arr[1]:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")