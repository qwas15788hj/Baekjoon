n = int(input())
pattern = input()
for _ in range(n):
    file = input()
    if len(pattern) - 1 > len(file):
        print("NE")
    else:
        idx = pattern.index("*")
        count = len(pattern) - 1 - idx
        if pattern[:idx] != file[:idx] or pattern[idx+1:] != file[len(file)-count:]:
            print("NE")
        else:
            print("DA")