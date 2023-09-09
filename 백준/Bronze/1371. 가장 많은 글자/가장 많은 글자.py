import sys
input = sys.stdin.read

s = input().replace("\n", "").replace(" ","") # 입력 후 띄어쓰기, 공백 제거
arr = [0] * 26 # 알파벳 배열
# 알파벳 갯수 찾기
for i in s:
    arr[ord(i) - 97] += 1

# 최대 개수
count = max(arr)

# 최대 개수 알파벳 찾기
answer = []
for i in range(len(arr)):
    if arr[i] == count:
        answer.append(chr(i + 97))

# 정렬 후 출력
answer.sort()
print(*answer, sep="")