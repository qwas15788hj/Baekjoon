# 플로이드 워셜
def solution(N, road, K):
    answer = 0
    
    # 무한 값을 갖는 2차원 배열 생성
    arr = [[1e9] * (N+1) for _ in range(N+1)]
    
    # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for i in range(1, N+1):
        arr[i][i] = 0
    
    # i <-> j 비용 최소화
    for i, j, k in road:
        arr[i][j] = min(arr[i][j], k)
        arr[j][i] = min(arr[j][i], k)
    
    # 플로이드 워셜
    # 경 - 출 - 도
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                # i -> j 최단 거리 = i -> j 직접 or i -> k -> j k 거쳐서
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
    
    # 1번에서 i까지 K보다 작으면 배달 가능
    for i in range(1, N+1):
        if arr[1][i] <= K:
            answer += 1
    
    return answer