def solution(arr):
    answer = [0, 0]
    
    # 압축하는 함수 생성 (세로, 가로, 길이)
    def comp(x, y, n):
        start = arr[x][y] # 시작점의 수
        # 세로, 가로 모두 n길이만큼 돌면서
        for i in range(x, x + n):
            for j in range(y, y + n):
                # 해당 위치가 시작점과 다르면 압축 실패
                if arr[i][j] != start:
                    n //= 2 # 길이 반으로
                    comp(x, y, n) # x, y 를 시작점으로 길이 반만큼 다시 comp함수 돌기
                    comp(x, y + n, n) # x, y + n 을 시작점으로 길이 반만큼 다시 comp함수 돌기
                    comp(x + n, y, n) # x + n, y 를 시작점으로 길이 반만큼 다시 comp함수 돌기
                    comp(x + n, y + n, n) # x + n, y + n 를 시작점으로 길이 반만큼 다시 comp함수 돌기
                    return
        # if문 안타면 압축 성공으로 시작점인 수 + 1
        answer[start] += 1
    
    # comp 함수 0, 0, arr 길이로 호출
    comp(0, 0, len(arr))
    
    return answer