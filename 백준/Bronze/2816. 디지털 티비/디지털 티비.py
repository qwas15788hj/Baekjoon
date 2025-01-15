import sys
input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]

answer = ""
idx = arr.index("KBS1")
answer += "1" * idx
answer += "4" * idx

arr.pop(idx)
arr.insert(0, "KBS1")

idx = arr.index("KBS2")
answer += "1" * idx
answer += "4" * (idx-1)

print(answer)