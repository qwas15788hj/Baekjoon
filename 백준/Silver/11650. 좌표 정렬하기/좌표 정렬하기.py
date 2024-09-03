arr = []
n = int(input())
for i in range(n):
    arr.append(list(map(int, input().split())))
    
arr.sort(key=lambda x:(x[0], x[1]))

for i in arr:
    print(i[0], i[1])