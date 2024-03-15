n = int(input())
start = list(map(int, input()))
target = list(map(int, input()))

def switch(bulb):
    bulb_sub = bulb[:]
    count = 0
    for i in range(1, n-1):
        if bulb_sub[i-1] != target[i-1]:
            count += 1
            for j in range(i-1, i+2):
                bulb_sub[j] = 1 - bulb_sub[j]

    if bulb_sub[n-1] != target[n-1]:
        count += 1
        bulb_sub[n-2] = 1 - bulb_sub[n-2]
        bulb_sub[n-1] = 1 - bulb_sub[n-1]

    if bulb_sub == target:
        return count
    else:
        return 1e9

answer = switch(start)
start[0] = 1 - start[0]
start[1] = 1 - start[1]
answer = min(answer, switch(start) + 1)

if answer != 1e9:
    print(answer)
else:
    print(-1)