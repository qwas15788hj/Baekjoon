s = input()
q = int(input())

# 알파벳 별 나온 횟수 누적 합 저장 배열
arr = [[0] * len(s) for _ in range(26)]
for i in range(26): # 총 열 26개 = 알파벳 개수
    for j in range(len(s)): # 총 행 = 문자열 s 개수
        if j != 0: # 누적 합을 위해 0이 아니면 이전꺼 그대로 유지
            arr[i][j] += arr[i][j-1]
        if s[j] == chr(97+i): # 해당 알파벳이면 + 1
            arr[i][j] += 1

for _ in range(q):
    a, l, r = map(str, input().split())
    if int(l) == 0: # 첫 시작이 0이면, 해당 알파벳의 r 지점만 출력
        print(arr[ord(a)-97][int(r)])
    else: # 첫 시작이 0이 아니면, 해당 알파벳의 r 지점 - l-1 지점 출력
        print(arr[ord(a)-97][int(r)] - arr[ord(a)-97][int(l)-1])