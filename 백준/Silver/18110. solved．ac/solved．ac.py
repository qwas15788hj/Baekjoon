import sys
input = sys.stdin.readline

n = int(input()) # 난이도 의견의 개수 n 입력
arr = [] # 의견 저장할 배열 생성
for _ in range(n): # n 반복
    arr.append(int(input())) # 배열에 의견 저장

arr.sort() # 의견 오름차순 정렬
count = round(n * 0.15 + 0.0000001) # 절사평균을 이용해 제외할 인원 수 구하기 (반올림)

# count 만큼 배열 앞뒤 제거
arr = arr[count:] # 배열 앞 제거
for _ in range(count): # 배열 뒤 제거
    arr.pop()

if n == 0: # 0 명일 경우
    print(0)
else: # 1개 이상일 경우
    # 배열에서 제외할 인원 수 앞뒤 제거 후 총합 구한 후
    # n 명에서 제외한 인원 수 (count * 2)명을 제외한 후 평균 구하기 (반올림)
    print(int(round(sum(arr) / (n - count * 2) + 0.00000001)))