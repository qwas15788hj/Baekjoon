class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        alpha = [0] * 26
        for i in range(n):
            alpha[ord(s[i])-97] += 1
        
        answer = ""
        flag = False
        for i in range(n):
            idx = ord(target[i])-97
            print(idx)
            # 같은게 있다면 앞에 배치
            if alpha[idx] > 0:
                alpha[idx] -= 1
                answer += target[i]
            # 같은게 없다면
            else:
                # 이번 target인 알파벳보다 큰 것 중 가장 작은 것 추가
                for j in range(idx+1, 26):
                    if alpha[j] > 0:
                        alpha[j] -= 1
                        answer += chr(j+97)
                        flag = True
                        break
            if flag:
                break

        # 남은 것 answer에 더하기
        for i in range(26):
            answer += (chr(i+97))*alpha[i]
        
        if answer <= target:
            return ""
        else:
            return answer