n = input()  # 문자열 입력
m = input()  # 폭발 문자열 입력
arr = [] # 배열(스택) 생성

for i in range(len(n)):  # 문자열 원소 하나씩 반복
    arr.append(n[i]) # 현재 원소 배열에 저장
    if n[i] == m[-1]:  # 현재 탐색할 원소가 폭발 문자열 끝자리와 같다면
        if "".join(arr[-(len(m)):]) == m: # 배열 끝자리 m만큼이 m과 같다면
            for _ in range(len(m)): # m만큼 배열에서 삭제
                arr.pop()

if arr: # 배열에 요소가 있다면
    print("".join(arr)) # 해당 요소를 붙여서 문자열로 출력
else: # 빈 배열이면
    print("FRULA")