n = int(input())
arr = [i for i in range(1, n+1)]

card = []
while len(arr) != 1:
    card.append(arr.pop(0))
    arr.append(arr.pop(0))

answer = card+arr
for i in answer:
    print(i, end=" ")