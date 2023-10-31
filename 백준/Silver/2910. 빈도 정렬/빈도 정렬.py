n, c = map(int, input().split())
arr = list(map(int, input().split()))
dic = dict() # 숫자가 나왔는지 체크
num = [] # 숫자 넣기
idx = 0 # 몇 번째 인지 체크

for a in arr: # 입력 숫자 돌면서
    if a not in dic: # 해당 숫자가 dic 에 없다면 -> 최초 등장이면
        dic[a] = idx # dic 에 해당 숫자 등장 순서 저장
        num.append([a, 1, idx]) # num 에는 [해당 숫자, 나온 횟수, 등장 순서] 저장
        idx += 1 # 등장 순서 증가
    else: # 이미 등장한 숫자라면
        num[dic[a]][1] += 1 # 해당 숫자의 등장 순서에 맞게 카운트 증가

# 나온 개수 내림차순, 등장 순서 오름차순 정렬
num.sort(key=lambda x:(-x[1], x[2]))

# num 배열 돌면서
for i in range(len(num)):
    for j in range(num[i][1]): # 해당 숫자 등장 만큼
        print(num[i][0], end=" ") # 해당 숫자 출력