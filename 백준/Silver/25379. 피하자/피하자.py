n = int(input())
arr = list(map(int, input().split()))

odd, even = [], []
for i in range(n):
    if arr[i] % 2 != 0:
        odd.append(i)
    else:
        even.append(i)

if n <= 2 or len(odd) == n or len(even) == n:
    print(0)
else:
    answer = 1e9
    count = 0
    for i in range(len(odd)):
        count += abs(odd[i]-i)
    answer = min(answer, count)

    count = 0
    for i in range(len(even)):
        count += abs(even[i]-i)
    answer = min(answer, count)

    print(answer)