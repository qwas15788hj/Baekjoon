s1 = input()
s2 = input()
s3 = input()

arr = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

answer = ""
answer += str(arr.index(s1))
answer += str(arr.index(s2))
answer = int(answer)
answer *= 10**arr.index(s3)

print(answer)