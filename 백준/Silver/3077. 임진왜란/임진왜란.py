n = int(input())
arr1 = list(map(str, input().split()))
arr2 = list(map(str, input().split()))
a = dict()
b = dict()

for i in range(n):
    a[arr1[i]] = i
    b[arr2[i]] = i

answer = 0
for i in range(n-1):
    for j in range(i+1, n):
        if (a[arr2[i]] > a[arr2[j]] and b[arr2[i]] > b[arr2[j]]) or (a[arr2[i]] < a[arr2[j]] and b[arr2[i]] < b[arr2[j]]):
            answer += 1

print(f'{answer}/{(n*(n-1))//2}')