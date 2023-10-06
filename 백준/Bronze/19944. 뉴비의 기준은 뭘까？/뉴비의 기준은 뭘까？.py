n, m = map(int, input().split()) # n, m 입력
if m == 1 or m == 2: # m 이 1이나 2면 뉴비
    print("NEWBIE!")
elif m <= n: # m 이 1이나 2가 아니고 n 보다 작거나 같으면 올드비
    print("OLDBIE!")
else: # 뉴비, 올드비 둘 다 아니면 TLE
    print("TLE!")