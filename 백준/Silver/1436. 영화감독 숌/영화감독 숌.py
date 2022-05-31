n = int(input())
six_num = 666
count = 0
while True:
    if "666" in str(six_num):
        count += 1
    if count == n:
        break
    six_num += 1

print(six_num)