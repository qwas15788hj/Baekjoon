def check(l, r):
    while True:
        if l == r or l-1 == r:
            return [l, r, True]
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return [l, r, False]

t = int(input())
for _ in range(t):
    s = input()
    left, right = 0, len(s)-1

    left, right, flag = check(left, right)
    l_l, l_r, left_flag = check(left+1, right)
    r_l, r_r, right_flag = check(left, right-1)

    if flag:
        print(0)
    else:
        if left_flag or right_flag:
            print(1)
        else:
            print(2)