t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(str, input().split()))

    word = arr[0]
    for i in range(1, len(arr)):
        if arr[i] + word > word + arr[i]:
            word = word + arr[i]
        else:
            word = arr[i] + word

    print(word)