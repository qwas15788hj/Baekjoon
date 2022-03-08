n = int(input())
arr = []
for _ in range(n):
    data = input().split()
    arr.append((str(data[0]), int(data[1]), int(data[2]), int(data[3])))
    
arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in arr:
    print(i[0])