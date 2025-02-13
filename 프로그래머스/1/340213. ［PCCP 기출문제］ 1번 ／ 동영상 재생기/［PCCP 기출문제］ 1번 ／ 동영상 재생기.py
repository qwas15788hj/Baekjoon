def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    v = int(video_len[:2])*60 + int(video_len[3:])
    p = int(pos[:2])*60 + int(pos[3:])
    s = int(op_start[:2])*60 + int(op_start[3:])
    e = int(op_end[:2])*60 + int(op_end[3:])
    
    if s <= p and p <= e:
        p = e
        
    for command in commands:
        if command == "next":
            p = min(p+10, v)
        else:
            p = max(p-10, 0)
        
        if s <= p and p <= e:
            p = e
    
    m = str(p//60)
    s = str(p%60)
    if len(m) == 1:
        m = "0" + m
    if len(s) == 1:
        s = "0" + s
    
    answer = m + ":" + s
    
    return answer