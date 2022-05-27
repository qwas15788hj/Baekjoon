for tc in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    command = list(input().split())
    for i in range(len(command)):
        if command[i] == "I":
            index = int(command[i+1])
            count = int(command[i+2])
            for j in range(count):
                arr.insert(index+j, int(command[i+2+j+1]))
        elif command[i] == "D":
            index = int(command[i+1])
            count = int(command[i+2])
            for _ in range(count):
                del arr[index]
        elif command[i] == "A":
            count = int(command[i+1])
            for j in range(1, count+1):
                arr.append(command[i+j+1])

    answer = " ".join(map(str, arr[:10]))
    print(f"{tc} {answer}")