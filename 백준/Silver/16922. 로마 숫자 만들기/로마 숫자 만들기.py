n = int(input())
answer = set()

for i in range(n+1):
    for j in range(n+1-i):
        for z in range(n+1-i-j):
            for k in range(n+1-i-j-z):
                if (i+j+z+k) == n:
                    answer.add(i*1 + j*5 + z*10 + k*50)

print(len(answer))