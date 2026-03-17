n = int(input())
for i in range(n):
    arr = list(input())
    alpha = [0] * 26
    for s in arr:
        if (97 <= ord(s) <= 122) or (65 <= ord(s) <= 90):
            s = s.lower()
            alpha[ord(s)-97] += 1

    count = min(alpha)
    if count == 0:
        print(f'Case {i+1}: Not a pangram')
    elif count == 1:
        print(f'Case {i+1}: Pangram!')
    elif count == 2:
        print(f'Case {i+1}: Double pangram!!')
    else:
        print(f'Case {i+1}: Triple pangram!!!')