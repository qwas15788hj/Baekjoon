from itertools import permutations

k = int(input())
arr = list(input().split())
number = [0,1,2,3,4,5,6,7,8,9]
result = []
for p in permutations(number, k+1):
    flag = True
    for i in range(len(arr)):
        if arr[i] == "<":
            if p[i] > p[i+1]:
                flag = False
                break
        else:
            if p[i] < p[i+1]:
                flag = False
                break
    if flag == True:
        result.append(p)

max_answer = "".join(map(str, max(result)))
min_answer = "".join(map(str, min(result)))
print(max_answer)
print(min_answer)