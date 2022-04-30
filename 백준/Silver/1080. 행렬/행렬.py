n, m = map(int, input().split())
a = []
b = []
for _ in range(n):
    a.append(list(map(int, input())))

for _ in range(n):
    b.append(list(map(int, input())))
    
def flip(i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            a[x][y] = 1-a[x][y]
            
count = 0
for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            flip(i, j)
            count += 1
        if a == b:
            break
    if a == b:
        break
        
if a == b:
    print(count)
else:
    print(-1)