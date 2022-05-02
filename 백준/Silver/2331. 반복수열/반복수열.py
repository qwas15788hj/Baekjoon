a, p = map(int, input().split())
d = [a]
while True:
    num_list = list(map(int, str(d[-1])))
    num = 0
    for i in num_list:
        num += i**p

    if num in d:
        break
    else:
        d.append(num)
print(d.index(num))