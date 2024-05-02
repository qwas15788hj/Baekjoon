n, k = map(int, input().split())
arr = list(map(int, input().split()))
check = []
for i in range(n-1):
    check.append(arr[i+1] - arr[i])

check.sort(reverse=True)
print(sum(check[k-1:]))