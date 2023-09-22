arr = [] # 알파벳 저장할 배열
size = 0 # 배열 중 가장 길이가 긴 배열의 길이

# 5줄 저장 후 size 갱신
for _ in range(5):
    s = list(input())
    size = max(size, len(s))
    arr.append(s)

# 5줄을 돌며 size 에 부족한 만큼 빈칸 채워주기
for i in range(5):
    if len(arr[i]) < size:
        for _ in range(size - len(arr[i])):
            arr[i].append("")

# 세로부터 출력
answer = ""
for i in range(size):
    for j in range(len(arr)):
        answer += arr[j][i]

print(answer)