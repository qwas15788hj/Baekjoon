arr = [0] * 31
for _ in range(28):
    arr[int(input())] = 1

for i in range(1, 31):
    if arr[i] == 0:
        print(i)