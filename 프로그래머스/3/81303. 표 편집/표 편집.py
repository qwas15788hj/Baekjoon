def solution(n, k, cmd):
    answer = ["O"] * n
    # 현재 위치의 이전과 다음 링크드리스트
    arr = {i: [i - 1, i + 1] for i in range(n)}
    stack = []
    
    for cm in cmd:
        c = cm.split(" ")
        # 현위치에서 링크드리스트 반복으로 타서 위쪽으로 오르기
        if c[0] == "U":
            for _ in range(int(c[1])):
                k = arr[k][0]
        
        # 링크드리스트로 내려가기
        elif c[0] == "D":
            for _ in range(int(c[1])):
                k = arr[k][1]
        
        # 현위치 제거
        elif c[0] == "C":
            # 현위치 stack에 저장
            prev, nxt = arr[k]
            answer[k] = "X"
            stack.append([prev, k, nxt])
            
            # 현재 위치 변경
            # 현위치가 끝번호면 앞으로 이동, 아니면 뒤로 이동
            if nxt == n:
                k = arr[k][0]
            else:
                k = arr[k][1]
            
            # 링크드리스트 변경
            # 현재 위치 링크드리스트의 값이 -1 이면, 다음 위치의 이전 값 -1로
            if prev == -1:
                arr[nxt][0] = prev
            # 현위치 링크드리스트의 값이 n으로 뒤가 없으면, 이전 위치의 다음 값 n으로
            elif nxt == n:
                arr[prev][1] = nxt
            # 앞뒤 둘 다 중간 위치로 이동 가능하면
            else:
                arr[prev][1] = nxt
                arr[nxt][0] = prev
                
        # 복구 작업
        else:
            prev, now, nxt = stack.pop()
            answer[now] = "O"
            
            if prev == -1:
                arr[nxt][0] = now
            elif nxt == n:
                arr[prev][1] = now
            else:
                arr[prev][1] = now
                arr[nxt][0] = now
    
    return "".join(answer)