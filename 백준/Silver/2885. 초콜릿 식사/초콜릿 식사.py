k = int(input())
num = bin(k)[2:]

if 2**(len(num)-1) == k:
    print(k, 0)
else:
    count = 0
    for i in range(len(num)):
        if num[i] == "1":
            count = i+1

    print(2**len(num), count)