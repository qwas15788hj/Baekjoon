n = int(input())
a = list(map(int, input().split()))
a.sort()
time = 0

for i in range(len(a)):
    time += sum(a[:i+1])
print(time)