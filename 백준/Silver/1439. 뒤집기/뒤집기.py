s = input()
zero_count = 0
one_count = 0
now = '2'

for i in s:
    if i == '0':
        if now != '0':
            zero_count += 1
        now = '0'
    else:
        if now != '1':
            one_count += 1
        now = '1'
print(min(zero_count, one_count))