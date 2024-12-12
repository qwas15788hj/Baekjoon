def hanoi(cnt, start, mid, end):
    if cnt == 1:
        print(f"{start} {end}")
        return

    hanoi(cnt-1, start, end, mid)
    print(f"{start} {end}")
    hanoi(cnt-1, mid, start, end)

n = int(input())
print(2**n-1)
hanoi(n, 1, 2, 3)