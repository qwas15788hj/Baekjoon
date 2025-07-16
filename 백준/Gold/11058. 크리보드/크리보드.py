n = int(input())

arr = [0] * (n+1)
for i in range(1, min(n+1, 7)):
    arr[i] = i

for i in range(7, n+1):
    arr[i] = max(arr[i-5]*4, arr[i-4]*3)
    
print(arr[-1])