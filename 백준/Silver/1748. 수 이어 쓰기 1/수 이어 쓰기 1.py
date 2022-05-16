n = input()
n_len = len(n)-1
answer = 0
i = 0
while i < n_len:
    answer += 9*(10**i)*(i+1)
    i += 1

answer += ((int(n) - (10**n_len)) +1) * (n_len+1)

print(answer)