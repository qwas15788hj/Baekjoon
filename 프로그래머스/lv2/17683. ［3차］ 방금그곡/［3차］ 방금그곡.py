def solution(m, musicinfos):
    answer = ""
    before = ["A#", "C#", "D#", "F#", "G#"]
    after = ["H", "I", "J", "K", "L"]
    for i in range(len(before)): # #이 포함된 음 바꿔주기
        m = m.replace(before[i], after[i])
    
    time = 0
    for musicinfo in musicinfos: # 모든 음악 돌면서
        music_list = musicinfo.split(",") # 현재 음악 리스트
        # 시작 시간
        start_time = int(music_list[0][0] + music_list[0][1]) * 60 + int(music_list[0][3] + music_list[0][4])
        # 종료 시간
        end_time = int(music_list[1][0] + music_list[1][1]) * 60 + int(music_list[1][3] + music_list[1][4])
        # 현재 음악 실행 시간
        music_time = end_time - start_time
        # 현재 음악의 음도 #없애기 위해 바꿔주기
        for i in range(len(before)):
            music_list[3] = music_list[3].replace(before[i], after[i])
        
        # 현재 음악의 총 재생 음
        music = (music_time // len(music_list[3])) * music_list[3] # 현재 음악의 모든 음이 반복된 만큼 저장
        music += music_list[3][:music_time % len(music_list[3])] # 이후 남은 음들을 저장
        
        if m in music: # 찾는 음이 현재 음악의 음에 있다면
            if music_time > time: # 현재 음악 시간이 기존(최종) 시간보다 길다면
                time = music_time # 최종 시간 갱신
                answer = music_list[2] # 음악 갱신
    
    # 모든 과정을 거쳐도 찾은 음악이 없다면
    if answer == "":
        answer = "(None)"
    
    return answer