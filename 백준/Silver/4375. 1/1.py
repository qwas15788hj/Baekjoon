while True:
    try:
        n = int(input())
    except:
        break
    
    num = "1"
    while int(num)%n != 0:
        num += "1"
    print(len(num))