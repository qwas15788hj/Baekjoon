while True :
    try :
        s = input()

        arr = [0] * 4
        for i in range(len(s)):
            if 'a' <= s[i] <= 'z':
                arr[0] += 1
            elif 'A' <= s[i] <= 'Z':
                arr[1] += 1
            elif '0' <= s[i] <= '9':
                arr[2] += 1
            else:
                arr[3] += 1

        print(*arr)
    except EOFError :
        break